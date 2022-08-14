import os
import json
import logging


from telegram.ext import Updater, CommandHandler

from model import model


CREDENTIALS_FILE = "credentials.txt"
TOKEN_FIELD = "auth-token"

COMMAND_HANDLERS = (
    CommandHandler("start", model.show_help),
    CommandHandler("hello", model.hello_name),
    CommandHandler("help", model.show_help),
    CommandHandler("rps", model.play_rps)
)


def start_bot():
    def init_bot():
        logger.debug("%s Checking credentials file", __name__)
        if not os.path.isfile(CREDENTIALS_FILE):
            raise FileNotFoundError(__name__, "No credentials file")
        logger.debug("%s Reading credentials file", __name__)
        with open(CREDENTIALS_FILE, 'r', encoding='utf-8') as f:
            cred_data = json.load(f)
        logger.debug("%s Registering credentials", __name__)
        updater = Updater(cred_data[TOKEN_FIELD])
        logger.debug("%s Registering command handlers", __name__)
        for command_handler in COMMAND_HANDLERS:
            updater.dispatcher.add_handler(command_handler)
        return updater

    logger = logging.getLogger("my_logger")

    updater = init_bot()
    logger.debug("%s Start polling", __name__)
    updater.start_polling()
    logger.debug("%s idle", __name__)
    updater.idle()
    