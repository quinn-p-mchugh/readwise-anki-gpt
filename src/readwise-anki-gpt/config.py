"""Module for storing config values used across the add-on."""

from pathlib import Path
from aqt import mw


ANKI_CONFIG = mw.addonManager.getConfig(__name__)

"""Paths & Directories"""
ADDON_ROOT_DIR = Path(__file__).parent
USER_DATA_DIR = ADDON_ROOT_DIR / "user_files"
DEPS_DIR = ADDON_ROOT_DIR / "deps"
USER_DATA_PATH = USER_DATA_DIR / "user_data.json"
USER_DATA_TEMPLATE_PATH = ADDON_ROOT_DIR / "user_data_template.json"
READWISE_EXPORT_DATA_PATH = USER_DATA_DIR / "temp_readwise_export.json"
CARDS_DATA_PATH = USER_DATA_DIR / "generated_cards.json"
READWISE_SQLITE_DATABASE_PATH = USER_DATA_DIR / "readwise_data.sqlite"

"""URLs"""
READWISE_ACCESS_TOKEN_URL = "https://readwise.io/access_token"

"""SQL Tables Names"""
TABLE_READWISE_BOOK = "ReadwiseBook"
TABLE_READWISE_HIGHLIGHT = "ReadwiseHighlight"
TABLE_READWISE_TAG = "ReadwiseTag"
TABLE_READWISE_HIGHLIGHT_TAG = "ReadwiseHighlightReadwiseTag"
TABLE_ANKI_CARD = "AnkiCard"
