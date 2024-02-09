import sqlite3
from . import config
from typing import Generator

def stream_records(db_conn: sqlite3.Connection, table_name: str) -> Generator[dict, None, None]:
    """
    Streams records from a specified SQLite table.

    Args:
        db_path: The file path to the SQLite database.
        table_name: The name of the table to stream records from.

    Yields:
        A generator of dictionary objects representing each row in the table.
    """
    db_conn.row_factory = sqlite3.Row 
    cur = db_conn.execute(f"SELECT * FROM {table_name}")
    for row in cur:
        yield dict(row)

def bulk_insert_records(db_conn: sqlite3.Connection, table_name: str, records: list[dict]):
    with db_conn as cur:
        placeholders = ', '.join(['?'] * len(records[0]))
        columns = ', '.join(records[0].keys())
        values = [tuple(record.values()) for record in records]
        cur.executemany(
            f'''
            INSERT INTO {table_name} ({columns}) 
            VALUES ({placeholders})''', 
            values
        )
            

def insert_card_into_db(db_conn: sqlite3.Connection, highlight_id: int, flashcard_front: str, flashcard_back: str):
    """
    Inserts the processed content into the Cards table.

    Args:
        db_conn (sqlite3.Connection): Active database connection.
        highlight_id (int): ID of the highlight being processed.
    """
    with db_conn as cur:
        cur.execute('''
            INSERT INTO AnkiCard (highlight_id, flashcard_front, flashcard_back) 
            VALUES (?, ?, ?)
            ''', 
            (highlight_id, flashcard_front, flashcard_back)
        )


def create_sqlite_tables(conn: sqlite3.Connection):
    with conn as cur:
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {config.TABLE_READWISE_BOOK} (
            user_book_id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            readable_title TEXT,
            source TEXT,
            cover_image_url TEXT,
            unique_url TEXT,
            category TEXT,
            document_note TEXT,
            readwise_url TEXT,
            source_url TEXT,
            asin TEXT
        )''')

    with conn as cur:
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {config.TABLE_READWISE_HIGHLIGHT} (
            id INTEGER PRIMARY KEY,
            text TEXT,
            location INTEGER,
            location_type TEXT,
            note TEXT,
            color TEXT,
            highlighted_at TEXT,
            created_at TEXT,
            updated_at TEXT,
            external_id INTEGER,
            end_location INTEGER,
            url TEXT,
            book_id INTEGER NOT NULL,
            is_favorite BOOLEAN,
            is_discard BOOLEAN,
            readwise_url TEXT,
            FOREIGN KEY(book_id) REFERENCES {config.TABLE_READWISE_BOOK}(user_book_id) ON DELETE CASCADE
        )''')

    with conn as cur:
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {config.TABLE_READWISE_TAG} (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )''')

    with conn as cur:
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {config.TABLE_READWISE_HIGHLIGHT_TAG} (
            highlight_id INTEGER NOT NULL,
            tag_id INTEGER NOT NULL,
            PRIMARY KEY(highlight_id, tag_id),
            FOREIGN KEY(highlight_id) REFERENCES {config.TABLE_READWISE_HIGHLIGHT}(id) ON DELETE CASCADE,
            FOREIGN KEY(tag_id) REFERENCES {config.TABLE_READWISE_TAG}(id) ON DELETE CASCADE
        )''')
    
    with conn as cur:
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {config.TABLE_ANKI_CARD} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            highlight_id INTEGER NOT NULL,
            flashcard_front TEXT NOT NULL,
            flashcard_back TEXT NOT NULL,
            FOREIGN KEY(highlight_id) REFERENCES {config.TABLE_READWISE_HIGHLIGHT}(id) ON DELETE CASCADE
        )''')
        