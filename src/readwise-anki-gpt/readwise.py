import json
import requests
import sqlite3

from . import config
from contextlib import closing
from .gui.msg_box import missing_rw_access_token
from datetime import datetime
from .database import create_sqlite_tables
from . import controller
from aqt import QObject
from aqt import pyqtSlot, pyqtSignal

# TODO: Add exception handling to this module

def fetch_readwise_highlights(access_token: str,  updated_after: datetime, page_cursor: str) -> object:
    """Export Readwise highlights to JSON using Readwise API.
    
    See "Highlight EXPORT" API call at https://readwise.io/api_deets

    Args:
        access_token (str): The Readwise access token of the desired user.
        updated_after (datetime): A date indicating which highlights should be included in the export. Highlights after this date will be included.
        page_cursor (str): A string returned by a previous request to the export endpoint. This is used to get the next page of highlights if there are too many for one request.

    Returns:
        object: A JSON object containing the desired Readwise highlights (grouped by source).
    """
    params = {}
    if page_cursor:
        params['pageCursor'] = page_cursor
    if updated_after:
        params['updatedAfter'] = updated_after
    
    response = requests.get(
        url="https://readwise.io/api/v2/export/",
        params=params,
        headers={"Authorization": f"Token {access_token}"}, verify=True
    )
    return response.json()

def export_readwise_highlights():
    """Exports all Readwise highlights from a user's account using the Readwise API.

    Returns:
        list[object]: All the user's Readwise highlights (grouped by source) as a JSON array.
    """
    readwise_access_token = config.ANKI_CONFIG['readwiseAccessToken']
    
    if not readwise_access_token:
        missing_rw_access_token()
    
    user_data = controller.read_user_data()
    
    #readwise = Readwise(readwise_access_token)
    export_full = []
    updated_after = ""
    next_page_cursor = None
    readwise_highlight_last_fetched_at = user_data["readwiseHighlightsLastFetchedAt"]
    updated_after = datetime.fromisoformat(readwise_highlight_last_fetched_at) if readwise_highlight_last_fetched_at else ""
    while True:
        export_partial = fetch_readwise_highlights(readwise_access_token, updated_after, next_page_cursor)
        export_full.extend(export_partial['results'])
        
        next_page_cursor = export_partial.get('nextPageCursor')
        if not next_page_cursor:
            break
        
    export_full = filter_highlight_data(export_full)
        
    rw_export_to_sqlite(export_full)
    
    user_data["readwiseHighlightsLastFetchedAt"] = datetime.now().isoformat()
    with open(config.USER_DATA_PATH, 'w', encoding="utf-8") as f:
        json.dump(user_data, f, indent=4)
        

def filter_highlight_data(highlights_export_json: list[object]) -> list[object]:
    """Filter Readwise highlights based on criteria specified by user.

    Args:
        highlights_export_json (list[object]): A JSON array of the user's Readwise highlights (grouped by source).

    Returns:
        list[object]: A filtered JSON array of the user's Readwise highlights (grouped by source).
    """
    highlight_tags_to_include = set(config.ANKI_CONFIG["readwiseHighlightTagsToInclude"])
    highlight_tags_to_exclude = set(config.ANKI_CONFIG["readwiseHighlightTagsToExclude"])
    document_tags_to_include = set(config.ANKI_CONFIG["readwiseDocumentTagsToInclude"])
    document_tags_to_exclude = set(config.ANKI_CONFIG["readwiseDocumentTagsToExclude"])
    
    all_tag_sets_empty = all(not s for s in [highlight_tags_to_include, highlight_tags_to_exclude, document_tags_to_include, document_tags_to_exclude])
    if all_tag_sets_empty:
        return highlights_export_json
    
    def tags_intersect(element_tags: set, tags_to_compare: set):
        """Check if the element has at least one tag from the tags to include list.

        Args:
            element_tags (set): A set of tags associated with the element.
            tags_to_compare (set): A set of tags compared against the element tags to check for intersection.

        Returns:
            bool: True if the element contains at least one tag from the tags to compare, False otherwise.
        """
        return not set(element_tags).isdisjoint(tags_to_compare)
    
    def include_element(element_tags: set, included_tags: set, excluded_tags: set):
        """Determine whether to include the element based on included and excluded tags.

        Args:
            element_tags (set): A set of tags associated with the element.
            included_tags (set): A set of tags to include.
            excluded_tags (set): A set of tags to exclude.

        Returns:
            bool: True if the element should be included, False otherwise.
        """
        return tags_intersect(element_tags, included_tags) or not tags_intersect(element_tags, excluded_tags)
    
    document_tag_key = "book_tags"
    if document_tags_to_include and document_tags_to_exclude:
        highlights_export_json = [source for source in highlights_export_json if include_element(source[document_tag_key], document_tags_to_include, document_tags_to_exclude)]
    elif document_tags_to_include:
        highlights_export_json = [source for source in highlights_export_json if tags_intersect(source[document_tag_key], document_tags_to_include)]
    elif document_tags_to_exclude:
        highlights_export_json = [source for source in highlights_export_json if not tags_intersect(source[document_tag_key], document_tags_to_exclude)]
        
    highlight_key = "highlights"
    highlight_tags_key = "tags"
    if highlight_tags_to_include and highlight_tags_to_exclude:
        for i, source in enumerate(highlights_export_json):
            highlights = source[highlight_key]
            if not highlights:
                continue
            highlights_export_json[i][highlight_key] = [highlight for highlight in highlights if include_element([tag["name"] for tag in highlight[highlight_tags_key]], highlight_tags_to_include, highlight_tags_to_exclude)]
    elif highlight_tags_to_include:
        for i, source in enumerate(highlights_export_json):
            highlights = source[highlight_key]
            if not highlights:
                continue
            highlights_export_json[i][highlight_key] = [highlight for highlight in highlights if tags_intersect([tag["name"] for tag in highlight[highlight_tags_key]], highlight_tags_to_include)]
    elif highlight_tags_to_exclude:
        for i, source in enumerate(highlights_export_json):
            highlights = source[highlight_key]
            if not highlights:
                continue
            highlights_export_json[i][highlight_key] = [highlight for highlight in highlights if not tags_intersect([tag["name"] for tag in highlight[highlight_tags_key]], highlight_tags_to_exclude)]
    highlights_export_json = [source for source in highlights_export_json if source[highlight_key]]   # Remove any sources that did NOT have any highlights that matched user's criteria
    
    return highlights_export_json

def read_highlights_data() -> list[object]:
    """Load Readwise highlights from local data file.

    Returns:
        list[object]: A JSON array containing the desired Readwise highlights (grouped by source).
    """
    if config.READWISE_EXPORT_DATA_PATH.exists():
        with open(config.READWISE_EXPORT_DATA_PATH, 'r') as f:
            return json.load(f)
    return []


def rw_export_to_sqlite(rw_export_data: list[object]):
    """Insert Readwise export data into SQLite database.

    Args:
        rw_export_json (list[object]): A JSON array containing the Readwise export data.
    """
    with sqlite3.connect(config.READWISE_SQLITE_DATABASE_PATH) as conn:
        create_sqlite_tables(conn)
        upsert_rw_data(conn, rw_export_data)

def upsert_rw_data(conn, rw_export_data):
    for book in rw_export_data:
        with conn as cur:
            cur.execute(f'''
                INSERT INTO {config.TABLE_READWISE_BOOK} (user_book_id, title, author, readable_title, source, cover_image_url, unique_url, category, document_note, readwise_url, source_url, asin)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(user_book_id) DO UPDATE SET
                    title = excluded.title,
                    author = excluded.author,
                    readable_title = excluded.readable_title,
                    source = excluded.source,
                    cover_image_url = excluded.cover_image_url,
                    unique_url = excluded.unique_url,
                    category = excluded.category,
                    document_note = excluded.document_note,
                    readwise_url = excluded.readwise_url,
                    source_url = excluded.source_url,
                    asin = excluded.asin
                ''', (
                book['user_book_id'], book['title'], book['author'], book['readable_title'],
                book['source'], book['cover_image_url'], book['unique_url'], book['category'],
                book['document_note'], book['readwise_url'], book['source_url'], book['asin']
            ))
            
        for highlight in book['highlights']:
            with conn as cur:
                cur.execute(f'''
                    INSERT INTO {config.TABLE_READWISE_HIGHLIGHT} (id, text, location, location_type, note, color, highlighted_at, created_at, updated_at, external_id, end_location, url, book_id, is_favorite, is_discard, readwise_url)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        text = excluded.text,
                        location = excluded.location,
                        location_type = excluded.location_type,
                        note = excluded.note,
                        color = excluded.color,
                        highlighted_at = excluded.highlighted_at,
                        created_at = excluded.created_at,
                        updated_at = excluded.updated_at,
                        external_id = excluded.external_id,
                        end_location = excluded.end_location,
                        url = excluded.url,
                        book_id = excluded.book_id,
                        is_favorite = excluded.is_favorite,
                        is_discard = excluded.is_discard,
                        readwise_url = excluded.readwise_url
                    ''', (
                    highlight['id'], highlight['text'], highlight['location'], highlight['location_type'],
                    highlight['note'], highlight['color'], highlight['highlighted_at'], highlight['created_at'],
                    highlight['updated_at'], highlight['external_id'], highlight['end_location'], highlight['url'],
                    highlight['book_id'], highlight['is_favorite'], highlight['is_discard'], highlight['readwise_url']
                ))
                
            for tag in highlight['tags']:
                with conn as cur:
                    cur.execute(f'''
                        INSERT INTO {config.TABLE_READWISE_TAG} (id, name)
                        VALUES (?, ?)
                        ON CONFLICT(id) DO NOTHING
                        ON CONFLICT(name) DO NOTHING;
                        ''',
                        (tag["id"], tag["name"])
                    )
                
                with conn as cur:
                    cur.execute(f'''
                        INSERT INTO {config.TABLE_READWISE_HIGHLIGHT_TAG} (highlight_id, tag_id)
                        VALUES (?, ?)
                        ON CONFLICT(highlight_id, tag_id) DO NOTHING;
                        ''', 
                        (highlight["id"], tag["id"]))
