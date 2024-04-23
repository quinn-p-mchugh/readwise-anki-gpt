"""Module for generating message boxes."""

from aqt import QMessageBox, QInputDialog, QStyle

from ..config import READWISE_ACCESS_TOKEN_URL


def missing_rw_access_token():
    """Display an error indicating the user has not provided a Readwise Access Token in the add-on's config file."""
    msg_box = QMessageBox(
        QMessageBox.Icon.Warning,
        "Missing Readwise Access Token",
        """Your Readwise Access Token is missing from the add-on configuration file.<br><br><a href="{READWISE_ACCESS_TOKEN_URL}">Get your Readwise Access Token</a>""",
        QMessageBox.StandardButton.Ok,
    )
    response = msg_box.exec()
    # TODO: Provide a button that open's the addon's config for the user - see here for details: https://www.reddit.com/r/Anki/comments/cx2zz1/how_can_i_open_the_config_with_an_addon/
    return response


def invalid_rw_access_token():
    """Display an error indicating the Readwise Access Token provided in the user's config is invalid."""
    msg_box = QMessageBox(
        QMessageBox.Icon.Warning,
        "Invalid Readwise Access Token",
        f"""An error occurred when attemping to use your Readwise Access Token.<br><br>Did your access token change? Was it added incorrectly?<br><br><a href="{READWISE_ACCESS_TOKEN_URL}">Get your Access Token</a>""",
        QMessageBox.StandardButton.Ok,
    )
    response = msg_box.exec()
    return response


def delete_all_data_confirmation():
    confirmation_text = "deletemydata"
    input_dialog = QInputDialog()
    input_dialog.setWindowIcon(
        input_dialog.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxWarning)
    )
    input_dialog.setWindowTitle("Warning: Data will be lost")
    input_dialog.setLabelText(
        f"""<html>You are about to:
        <b><ul>
            <li>Delete ALL Readwise highlights stored within Anki</li>
        </ul></b>
        <br>
        <p>This will NOT delete highlights in Readwise. In addition, all Anki cards created with this add-on will remain in Anki.
        
        <br><br><b>Are you sure you want to do this?</b><br>If so, type '{confirmation_text}' to confirm:</p></html>"""
    )
    input_dialog.setOkButtonText("Delete My Data")

    while True:
        ok = input_dialog.exec()
        input = input_dialog.textValue()

        if ok and input == confirmation_text:
            return True
        elif not ok:
            return False
        else:
            QMessageBox.warning(
                None,
                "Incorrect Input",
                f"Your input was incorrect.<br><br>Please type '{confirmation_text}' to confirm.",
            )
