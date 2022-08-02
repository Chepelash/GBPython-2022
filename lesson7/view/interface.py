from controller import controller
from logger import logger

def start_program_loop():
    HELP_TEXT = """Калькулятор. Выполняет операции с рациональными и комплексными числами.
Опции: 
h - вывести этот текст
q - выйти из программы
числа - разные режимы работы"""
    user_input = ""
    print(HELP_TEXT)
    print()
    while user_input.lower() != 'q':
        user_input = input("""Введите 1 для работы с рациональными числами
Введите 2 для работы с комплексными числами 
h - для вывода помощи
q - для выхода > """)
        if user_input == '1':
            logger.log_user_request(__name__, "Rational numbers operation")
            user_input = input("Наберите выражение > ")
            logger.log_user_request(__name__, user_input)
            try:
                print(f"Result = {controller.rational_operation(user_input)}")
            except ValueError as e:
                logger.log_error(e.args[0], e.args[1])
                print("Ошибка во вводе выражения")
            except ZeroDivisionError as e:
                logger.log_error(e.args[0], e.args[1])
                print("Деление на ноль")
            except Exception as e:
                logger.log_error(e.args[0], e.args[1])
                print("Неизвестная ошибка")
            
        elif user_input == '2':
            print("Работа с комплексными числами")
            print("Запись числел должна быть в виде 'a+bj'")
            print("""Список операций
1 - сложение
2 - разность
3 - умножение
4 - деление""")
            logger.log_user_request(__name__, "Complex numbers operation")

            a_number = input("Введите первое комплексное число > ").replace(" ", "")
            logger.log_user_request(__name__, f"a_number = {a_number}")
            b_number = input("Введите второе комплексное число > ").replace(" ", "")
            logger.log_user_request(__name__, f"b_number = {b_number}")
            operation = input("Введите номер операции > ")
            logger.log_user_request(__name__, f"operation = {operation}")

            try:
                print(f"Результат = {controller.complex_operation(a_number, b_number, operation)}")
            except ValueError as e:
                logger.log_error(e.args[0], e.args[1])
                print("Ошибка во вводе")
            except NotImplementedError as e:
                logger.log_error(e.args[0], e.args[1])
                print("Операция не существует")
            except Exception as e:                
                logger.log_error(e.args[0], e.args[1])
                print("Неизвестная ошибка")
        elif user_input.lower() == 'q':
            print("Выход из программы")
            logger.log_user_request(__name__, "Quitting")
            continue
        elif user_input.lower() == 'h':
            print(HELP_TEXT)
        else:
            print("Неизвестная команда")
