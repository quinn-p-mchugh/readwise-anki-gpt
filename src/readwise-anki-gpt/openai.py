"""Module for generating Anki cards from Readwise highlights using generative AI."""

import traceback
import sqlite3
import itertools
import json
from openai import OpenAI
from aqt.qt import QObject, pyqtSignal, QMessageBox

from . import config
from .database import stream_records, bulk_insert_records

from concurrent.futures import ThreadPoolExecutor, as_completed

class MessageBoxSignal(QObject):
    show_message = pyqtSignal(object, str, str, object)

message_box_signal = MessageBoxSignal()

def show_message(icon, title, text, buttons):
    msg_box = QMessageBox()
    msg_box.setIcon(icon)
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.setStandardButtons(buttons)
    msg_box.exec()

message_box_signal.show_message.connect(show_message)

def generate_cards():
    """Generate Anki cards from Readwise highlights using OpenAI API.
    """
    with sqlite3.connect(config.READWISE_SQLITE_DATABASE_PATH) as conn:
        highlight_records = stream_records(conn, config.TABLE_READWISE_HIGHLIGHT)
        limited_records = itertools.islice(highlight_records, 10)
        openai_client = OpenAI(api_key=config.ANKI_CONFIG["openaiApiKey"])
        card_records = []
        try:
            with ThreadPoolExecutor() as executor:
                futures = {executor.submit(generate_card, openai_client, highlight_record): highlight_record for highlight_record in limited_records}
                for future in as_completed(futures):
                    try:
                        highlight_record = futures[future]
                        key_value = {"highlight_id": highlight_record["id"]}
                        cards = future.result()
                        if not isinstance(cards, list):
                            cards = [cards]
                        for card in cards:
                            card.update(key_value)
                        card_records.extend(cards)
                    except Exception:
                        message_box_signal.show_message.emit(QMessageBox.Icon.Information, "Error 1", traceback.format_exc(), QMessageBox.StandardButton.Ok)
                        
                bulk_insert_records(conn, config.TABLE_ANKI_CARD, card_records)
        except Exception as e:
            message_box_signal.show_message.emit(QMessageBox.Icon.Information, "Error 2", traceback.format_exc(), QMessageBox.StandardButton.Ok)

def generate_card(openai_client: OpenAI, highlight_record: dict) -> dict:
    completion = openai_client.chat.completions.create(
        model=config.ANKI_CONFIG["openaiModel"],
        response_format={"type": "json_object"},
        temperature=config.ANKI_CONFIG["openaiModelTemperature"],
        messages=[
            {"role": "system", "content": config.ANKI_CONFIG["gpt_prompt"]},
            {"role": "system", "content": "\n\nALWAYS output your response as a JSON array in the format below, where each item in the array corresponds to a flashcard:\n\n[\n    {\n        \"flashcard_front\": \"\",\n        \"flashcard_back\": \"\",\n    }\n]"},
            {"role": "user", "content": f"\n\nPlease create one or more flashcards based on the text delimited by triple backticks:\n```{highlight_record['text']}```"}
        ]
    )
    
    try:
        choice = completion.choices[0]
        response_json_array = json.loads(choice.message.content) # TODO: Add exception handling if completion does not return valid JSON
    except json.JSONDecodeError:
         message_box_signal.show_message.emit(QMessageBox.Icon.Warning, "JSON Decode Error", f"{json.dumps(choice, indent=4)}<br><br>{traceback.format_exc()}", QMessageBox.StandardButton.Ok)
    
    return response_json_array
