from collections import OrderedDict
from logger import logger
from types import FunctionType


def show_dict_data(controller_function: FunctionType):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return
    except ValueError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Ошибка в заполнении данных")        
        return
    except FileNotFoundError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Отсутствуют файлы БД")        
        return
    except Exception as e:
        logger.log_error(__name__, e)
        print("Неизвестная ошибка")
        return
    for v in data.values():
        print(" ".join(list(v.values())))
        

def import_table(controller_function: FunctionType):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return
    except ValueError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Импортируемые таблицы не валидны")
        return
    except Exception as e:
        logger.log_error(__name__, e)
        print("Неизвестная ошибка")
        return
    print("OK")


def export_table(controller_function: FunctionType):
    try:
        data = controller_function()
    except NotImplementedError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Не сделано")
        return
    except ValueError as e:
        logger.log_error(e.args[0], e.args[1])
        print("Папка не существует")
        return
    except Exception as e:
        logger.log_error(__name__, e)
        print("Неизвестная ошибка")
        return
    for line in data:
        print(line)
