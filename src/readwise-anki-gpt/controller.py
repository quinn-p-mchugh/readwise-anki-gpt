

from datetime import datetime
import json
import os
import sys
import shutil

from aqt import mw
from aqt.utils import qconnect
from aqt.qt import QAction, QMenu, QMessageBox

from .gui.msg_box import *

from . import config
from .readwise import export_readwise_highlights
from .openai import generate_cards

def gen_cards_from_rw_highlights():
    """Generate Anki cards from Readwise highlights using OpenAI GPT."""
            
    export_readwise_highlights() # TODO: Implement progress bar for Readwise highlight export/database export/record insertion
    generate_cards() # TODO: Implement progress bar for card generation


def read_user_data():
    """Reads file containing user data. If user data file does not exist, create one based off of template."""
    if not config.USER_DATA_PATH.exists():
        if config.USER_DATA_TEMPLATE_PATH.exists():
            shutil.copy(config.USER_DATA_TEMPLATE_PATH, config.USER_DATA_PATH)
        else:
            raise FileNotFoundError("Add-on tried creating a new user data file, but template file was not found.<br><br>Please reinstall add-on and report this as a bug.")
    
    with open(config.USER_DATA_PATH, 'r') as f:
        return json.load(f)


def delete_all_data():
    files_to_delete = [
        config.READWISE_EXPORT_DATA_PATH,
        config.USER_DATA_PATH,
        config.READWISE_SQLITE_DATABASE_PATH,
    ]
    if not any([file.exists() for file in files_to_delete]):
        QMessageBox(
            QMessageBox.Icon.Information,
            "Error: No data to delete",
            "There is no data to delete!<br><br>Add-on is ready to generate cards from your Readwise highlights.",
            QMessageBox.StandardButton.Ok,
        ).exec()
        return 
    
    if delete_all_data_confirmation():
        [file.unlink(missing_ok=True) for file in files_to_delete]
        QMessageBox(
            QMessageBox.Icon.Information,
            "Success!",
            "All add-on data has been deleted.<br><br>Ah... a fresh start! ☺️",
            QMessageBox.StandardButton.Ok,
        ).exec()
        
        