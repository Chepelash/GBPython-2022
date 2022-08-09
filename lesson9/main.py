from view import interface
import settings
import logging
import logging.config

def main():
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    logger = logging.getLogger("my_logger")
    logger.info("%s Starting Program", __name__)
    interface.bot_loop()
    logger.info("%s Quitting Program", __name__)


if __name__ == "__main__":
    main()
