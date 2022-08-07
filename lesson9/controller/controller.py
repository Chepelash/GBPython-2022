import os
import json
import logging


from telegram.ext import Updater, CommandHandler

from model import model


CREDENTIALS_FILE = "credentials.txt"
TOKEN_FIELD = "auth-token"

COMMAND_HANDLERS = (
    CommandHandler("hello", model.hello_name),
    CommandHandler("help", model.show_help),
    CommandHandler("rps", model.play_rps)
)


def start_bot():
    def init_bot():
        if not os.path.isfile(CREDENTIALS_FILE):
            raise FileNotFoundError(__name__, "No credentials file")
        with open(CREDENTIALS_FILE, 'r', encoding='utf-8') as f:
            cred_data = json.load(f)
        updater = Updater(cred_data[TOKEN_FIELD])
        for command_handler in COMMAND_HANDLERS:
            updater.dispatcher.add_handler(command_handler)
        return updater

    updater = init_bot()
    updater.start_polling()
    updater.idle()
    