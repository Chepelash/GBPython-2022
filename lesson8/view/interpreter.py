from logger import logger


def show_dict_data(controller_function: function):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return


def import_table(controller_function: function):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return


def export_table(controller_function: function):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return