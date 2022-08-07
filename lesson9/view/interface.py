import logging

from controller import controller


def bot_loop():
    try:
        controller.start_bot()
    except FileNotFoundError as e:
        print("cred")
    except TypeError as e:
        print("Json")
    except Exception as e:
        print(e)
