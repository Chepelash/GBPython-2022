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
    while user_input.lower() != 'q':
        user_input = input("""Введите 1 для работы с рациональными числами
Введите 2 для работы с комплексными числами 
h - для вывода помощи
q - для выхода > """)
        if user_input == '1':
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
            a_number = input("Введите первое комплексное число > ").replace(" ", "")
            b_number = input("Введите второе комплексное число > ").replace(" ", "")
            operation = input("Введите операцию > ")
            try:
                controller.complex_operation(a_number, b_number, operation)
            except Exception as e:
                print("TODO Here")
        elif user_input.lower() == 'q':
            print("Выход из программы")
            continue
        elif user_input.lower() == 'h':
            print(HELP_TEXT)
        else:
            print("Неизвестная команда")            
