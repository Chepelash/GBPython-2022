from logger import logger
from controller import controller
from view import interpreter


def start_programm_loop():
    HELP_TEXT = """Программа управления персоналом
Команды:
q - выход
h - вывести этот текст
числа - команды меню"""

    def worker_menu():
        sub_menu_input = ""
        while sub_menu_input.lower != 'u':
            print()
            print("Меню работы с работниками")
            print("""Введите операцию
u - перейти в меню выше
1 - вывести всю таблицу работников
2 - добавить работника
3 - удалить работника
4 - изменить данные работника
""")
            sub_menu_input = input("> ")
            logger.log_user_request(__name__, sub_menu_input)
            if sub_menu_input == '1':
                interpreter.show_dict_data(controller.show_all_workers)
            elif sub_menu_input == '2':
                interpreter.show_dict_data(controller.add_new_worker)
            elif sub_menu_input == '3':
                interpreter.show_dict_data(controller.remove_worker)
            elif sub_menu_input == '4':
                interpreter.show_dict_data(controller.change_worker_data)
            elif sub_menu_input.lower() == 'u':
                print("Перемещаемся в меню выше")
            else:
                print("Неизвестная команда")


    def department_menu():
        sub_menu_input = ""
        while sub_menu_input.lower != 'u':
            print()
            print("Меню работы с отделами")
            print("""Введите операцию
u - перейти в меню выше
1 - вывести всю таблицу отделов
2 - добавить отдел
3 - удалить отдел
4 - изменить данные отдела
""")
            sub_menu_input = input("> ")
            logger.log_user_request(__name__, sub_menu_input)
            if sub_menu_input == '1':
                interpreter.show_dict_data(controller.show_all_departments)
            elif sub_menu_input == '2':
                interpreter.show_dict_data(controller.add_new_department)
            elif sub_menu_input == '3':
                interpreter.show_dict_data(controller.remove_department)
            elif sub_menu_input == '4':
                interpreter.show_dict_data(controller.change_department_data)
            elif sub_menu_input.lower() == 'u':
                print("Перемещаемся в меню выше")
            else:
                print("Неизвестная команда")

    def job_menu():
        sub_menu_input = ""
        while sub_menu_input.lower() != 'u':
            print()
            print("Меню работы с должностями")
            print("""Введите операцию
u - перейти в меню выше
1 - вывести всю таблицу должностей
2 - добавить должность
3 - удалить должность
4 - изменить данные должности
""")
            sub_menu_input = input("> ")
            logger.log_user_request(__name__, sub_menu_input)
            if sub_menu_input == '1':
                interpreter.show_dict_data(controller.show_all_jobs)
            elif sub_menu_input == '2':
                interpreter.show_dict_data(controller.add_new_job)
            elif sub_menu_input == '3':
                interpreter.show_dict_data(controller.remove_job)
            elif sub_menu_input == '4':
                interpreter.show_dict_data(controller.change_job_data)
            elif sub_menu_input.lower() == 'u':
                print("Перемещаемся в меню выше")
            else:
                print("Неизвестная команда")

    print(HELP_TEXT)
    user_input = ''
    print()
    while user_input.lower() != 'q':
        print()
        print("Главное меню")
        print("Введите команду для перехода в другое меню")
        print("""1 - операции с работниками
2 - операции с департаментами
3 - операции с должностями
4 - импортировать таблицу
5 - экспортировать таблицу
h - вывести помощь
q - выйти из программы""")
        user_input = input("> ")
        logger.log_user_request(__name__, user_input)
        if user_input == '1':
            worker_menu()
        elif user_input == '2':
            department_menu()
        elif user_input == '3':
            job_menu()
        elif user_input == '4':
            interpreter.import_table(controller.import_table)
        elif user_input == '5':
            interpreter.export_table(controller.export_table)
        elif user_input.lower() == 'h':
            print(HELP_TEXT)
        elif user_input.lower == 'q':
            print("Выход из программы.")
        else:
            print("Неизвестная команда")

