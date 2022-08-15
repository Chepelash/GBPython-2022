import logging

from model import model


def start_bot():
    logger = logging.getLogger("my_logger")

    updater = model.init_bot()
    logger.debug("Start polling")
    updater.start_polling()
    logger.debug("idle")
    updater.idle()
    