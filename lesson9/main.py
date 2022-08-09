from view import interface
import settings
import logging
import logging.config

def main():
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    logger = logging.getLogger("my_logger")
    logger.info("Starting Program")
    interface.bot_loop()
    logger.info("Quitting Program")


if __name__ == "__main__":
    main()
