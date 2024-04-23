import requests
import sqlite3
import logging

from . import config
from .gui.msg_box import missing_rw_access_token
from datetime import datetime
from .database import create_sqlite_tables
from . import controller

from aqt import QObject
from aqt import pyqtSlot, pyqtSignal

logging.basicConfig(level=logging.ERROR)

# TODO: Add exception handling to this module


def fetch_readwise_highlights(
    access_token: str, updated_after: datetime, page_cursor: str
) -> object:
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
        params["pageCursor"] = page_cursor
    if updated_after:
        params["updatedAfter"] = updated_after

    response = requests.get(
        url="https://readwise.io/api/v2/export/",
        params=params,
        headers={"Authorization": f"Token {access_token}"},
        verify=True,
    )

    return response.json()


def export_readwise_highlights():
    """Exports all Readwise highlights from a user's account using the Readwise API.

    Returns:
        list[object]: All the user's Readwise highlights (grouped by source) as a JSON array.
    """
    readwise_access_token = config.ANKI_CONFIG["readwiseAccessToken"]

    if not readwise_access_token:
        missing_rw_access_token()

    user_data = controller.read_user_data()

    # readwise = Readwise(readwise_access_token)
    export_full = []
    updated_after = ""
    next_page_cursor = None
    readwise_highlight_last_fetched_at = user_data["readwiseHighlightsLastFetchedAt"]
    updated_after = (
        datetime.fromisoformat(readwise_highlight_last_fetched_at)
        if readwise_highlight_last_fetched_at
        else ""
    )
    while True:
        export_partial = fetch_readwise_highlights(
            readwise_access_token, updated_after, next_page_cursor
        )
        export_full.extend(export_partial["results"])

        next_page_cursor = export_partial.get("nextPageCursor")
        if not next_page_cursor:
            break

    save_readwise_fetch_time(user_data)

    return export_full


def save_readwise_fetch_time(user_data: object):
    """Save Readwise fetch timestamp.

    Args:
        user_data (object): The user data
    """
    user_data["readwiseHighlightsLastFetchedAt"] = datetime.now().isoformat()
    controller.write_user_data(user_data)


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
            cur.execute(
                f"""
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
                """,
                (
                    book["user_book_id"],
                    book["title"],
                    book["author"],
                    book["readable_title"],
                    book["source"],
                    book["cover_image_url"],
                    book["unique_url"],
                    book["category"],
                    book["document_note"],
                    book["readwise_url"],
                    book["source_url"],
                    book["asin"],
                ),
            )

        for highlight in book["highlights"]:
            with conn as cur:
                cur.execute(
                    f"""
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
                    """,
                    (
                        highlight["id"],
                        highlight["text"],
                        highlight["location"],
                        highlight["location_type"],
                        highlight["note"],
                        highlight["color"],
                        highlight["highlighted_at"],
                        highlight["created_at"],
                        highlight["updated_at"],
                        highlight["external_id"],
                        highlight["end_location"],
                        highlight["url"],
                        highlight["book_id"],
                        highlight["is_favorite"],
                        highlight["is_discard"],
                        highlight["readwise_url"],
                    ),
                )

            for tag in highlight["tags"]:
                with conn as cur:
                    cur.execute(
                        f"""
                        INSERT INTO {config.TABLE_READWISE_TAG} (id, name)
                        VALUES (?, ?)
                        ON CONFLICT(id) DO NOTHING
                        ON CONFLICT(name) DO NOTHING;
                        """,
                        (tag["id"], tag["name"]),
                    )

                with conn as cur:
                    cur.execute(
                        f"""
                        INSERT INTO {config.TABLE_READWISE_HIGHLIGHT_TAG} (highlight_id, tag_id)
                        VALUES (?, ?)
                        ON CONFLICT(highlight_id, tag_id) DO NOTHING;
                        """,
                        (highlight["id"], tag["id"]),
                    )


export_readwise_highlights()
