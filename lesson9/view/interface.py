import logging

from controller import controller


def bot_loop():
    logger = logging.getLogger("my_logger")
    try:
        controller.start_bot()
    except FileNotFoundError as e:
        print("Cannot find credential file. Should be in credentials.txt")
        logger.error(e)
    except TypeError as e:
        logger.error(e)
        print("Json")
    except Exception as e:
        logger.error(e)
        print(e)
