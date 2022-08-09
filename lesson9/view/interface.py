import logging

from controller import controller


def bot_loop():
    logger = logging.getLogger("my_logger")
    try:
        controller.start_bot()
    except FileNotFoundError as e:
        print("Cannot find credential file. Should be in credentials.txt")
        logger.error("%s %s", __name__, e.strerror)
    except TypeError as e:
        logger.error("%s %s", __name__, e.strerror)
        print("Json")
    except Exception as e:
        logger.error("%s %s", __name__, e.strerror)
        print(e)
