import random



def task1():
    """Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
    """
    my_list = [x for x in range(100) if random.randint(0, 1)] + [chr(x) for x in range(100) if random.randint(0, 1)]
    print(my_list)
    number_to_find_str = input("Enter a number to find > ")
    try:
        number_to_find = int(number_to_find_str)
    except ValueError:
        print("Wrong input")
        return
    
    if number_to_find in my_list:
        print("It is in")
    else:
        print("It is not in")
    


def task2():
    """Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
    """
    pass


def task3():
    """Программа должна считывать одну строку со стандартного ввода 
    и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) 
    в формате "слово количество" (см. пример вывода).
    """
    pass


def main():
    task_list = [task1, task2, task3]
    for task in task_list:
        print(f"{task.__name__}...")
        task()
        print("Done\n")


if __name__ == "__main__":
    main()
