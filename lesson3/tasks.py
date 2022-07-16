import random
import string


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
    my_list = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 5))) for _ in range(random.randint(0, 7))]
    if random.randint(0, 5) and len(my_list) != 0:
        my_list.append(my_list[random.randrange(0, len(my_list))])        
    print(my_list)
    
    string_to_find = input("Enter a string to find second entrance > ")
    result = 0
    if my_list.count(string_to_find) < 2:
        result = -1
    else:
        result = my_list.index(string_to_find, my_list.index(string_to_find)+1)
    print(f"Index = {result}")


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
