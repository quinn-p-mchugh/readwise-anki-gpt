"""Main add-on module"""

import sys
from . import config
from aqt import mw
from aqt import qconnect
from aqt import QAction
from .controller import launch_addon_ui

sys.path.append(str(config.DEPS_DIR))


def build_menu():
    action_launch_addon_ui = QAction("Readwise Anki GPT", mw)
    mw.form.menuTools.addAction(action_launch_addon_ui)

    qconnect(action_launch_addon_ui.triggered, launch_addon_ui)


build_menu()
