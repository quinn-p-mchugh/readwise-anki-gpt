"""Main add-on module"""

import sys
from . import config
from aqt import mw
from aqt.utils import qconnect
from aqt.qt import QMenu, QAction
from .controller import delete_all_data, gen_cards_from_rw_highlights

sys.path.append(str(config.DEPS_DIR))

def build_menu():
    menu_addon = QMenu("Readwise Anki GPT", mw)
    action_gen_cards = QAction("Generate Cards from Readwise Highlights", mw)
    action_delete_data = QAction("Delete ALL DATA", mw)

    mw.form.menuTools.addMenu(menu_addon)
    menu_addon.addAction(action_gen_cards)
    menu_addon.addAction(action_delete_data)
    
    qconnect(action_gen_cards.triggered, gen_cards_from_rw_highlights)
    qconnect(action_delete_data.triggered, delete_all_data)
    
build_menu()

