from logger import logger
from types import FunctionType


def show_dict_data(controller_function: FunctionType):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return
    print(data)


def import_table(controller_function: FunctionType):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return
    print(data)


def export_table(controller_function: FunctionType):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return
    print(data)