from datetime import datetime
import json
import os
import sys
import shutil

from aqt import (
    mw,
    qconnect,
    QMessageBox,
    QDialog,
    QThreadPool,
    pyqtSlot,
    pyqtSignal,
    QRunnable,
    QObject,
)

from .gui.msg_box import *
from .designer import readwise_anki_gpt_ui, import_readwise_highlights_progress_bar_ui
from . import config


def read_user_data():
    """Reads file containing user data. If user data file does not exist, create one based off of template."""
    if not config.USER_DATA_PATH.exists():
        if config.USER_DATA_TEMPLATE_PATH.exists():
            shutil.copy(config.USER_DATA_TEMPLATE_PATH, config.USER_DATA_PATH)
        else:
            raise FileNotFoundError(
                "Add-on tried creating a new user data file, but template file was not found.<br><br>Please reinstall add-on and report this as a bug."
            )

    with open(config.USER_DATA_PATH, "r") as f:
        return json.load(f)


from .readwise import export_readwise_highlights, rw_export_to_sqlite
from .openai import generate_cards


class AddonUI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = readwise_anki_gpt_ui.Ui_ReadwiseAnkiGPT()
        self.ui.setupUi(self)

        self.thread_pool = QThreadPool()

        self.ui.readwiseImportHighlightsButton.pressed.connect(
            self.import_readwise_highlights
        )

    @pyqtSlot(int)
    def update_progress_bar(self, value):
        self.progress_bar_dialog.progressBar.setValue(value)

    @pyqtSlot()
    def import_readwise_highlights(self):
        """Import Readwise highlights as JSON and sqlite."""
        self.ui.readwiseImportHighlightsButton.setEnabled(False)

        class ProgressBarDialog(QDialog):

            def __init__(self):
                super().__init__()
                self.ui = (
                    import_readwise_highlights_progress_bar_ui.Ui_ReadwiseImportHighlightsProgressBar()
                )
                self.ui.setupUi(self)

                self.ui.progressBar.setValue(0)

        class WorkerSignals(QObject):
            update_progress = pyqtSignal(int)
            finished = pyqtSignal()

        class Worker(QRunnable):

            def __init__(self):
                super().__init__()
                self.signals = WorkerSignals()

            def run(self):
                rw_highlight_data = export_readwise_highlights()
                rw_export_to_sqlite(rw_highlight_data)

        def finished():
            self.ui.readwiseImportHighlightsButton.setEnabled(True)
            self.progress_bar_dialog.accept()

        self.worker = Worker()
        self.worker.signals.update_progress.connect(self.update_progress_bar)

        self.worker.signals.finished.connect(finished)
        self.progress_bar_dialog = ProgressBarDialog()
        self.progress_bar_dialog.ui.buttonBox.rejected.connect(
            finished
        )  # TODO: In the import highlights function, I'll need to check whether or not the above finished signal is set in order to make sure thread ends properly
        self.thread_pool.start(self.worker)
        self.progress_bar_dialog.exec()


def launch_addon_ui():
    """Launch addon UI."""
    addon_ui = AddonUI().exec()


def gen_cards_from_rw_highlights():
    """Generate Anki cards from Readwise highlights using OpenAI GPT."""

    import_readwise_highlights()  # TODO: Implement progress bar for Readwise highlight export/database export/record insertion
    generate_cards()  # TODO: Implement progress bar for card generation


def write_user_data(user_data: object):
    """Write data to user data file. To be used in conjunction with read_user_data method.

    Args:
        user_data (object): A JSON-like object containing the data to be written.
    """
    with open(config.USER_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=4)


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
