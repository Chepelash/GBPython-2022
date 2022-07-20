
import random


def task1():
    """Вычислить результат деления двух чисел c заданной точностью d"""
    input_precision_string = input("Enter a precision $10^{-1} ≤ d ≤10^{-10}$ > ")
    try:
        input_precision = int(input_precision_string)
    except ValueError:
        print("Wrong input")
        return
    if input_precision > -1 or input_precision < -10:
        print("Precision must be between -1 and -10")
        return
    
    input_numbers_string = input("Enter two numbers separated by space > ")
    try:
        num1, num2 = map(float, input_numbers_string.split(" "))
    except ValueError:
        print("Wrong input")
        return
    print(f"num1 / num2 = {round(num1/num2, input_precision * (-1))}")


def task2():
    """Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""
    def is_number_prime(number: int) -> bool:
        if number < 1:
            return True
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    N = random.randrange(100, 1000)
    counter = N
    simple_delimiters = set()
    for i in range(2, N):
        if not is_number_prime(i):
            continue
        if counter % i == 0:
            counter = counter / i
            simple_delimiters.add(i)
    print(f"N = {N}; ", end="")
    if not simple_delimiters:
        print("there is no prime delimiters")
    else:
        print(f"prime delimiters = {simple_delimiters}")
     


def task3():
    """Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча 
    и выводит на стандартный вывод сводную таблицу результатов всех матчей."""
    pass


def main():
    task_list = [task1, task2, task3]
    for task in task_list:
        print(f"{task.__name__}...")
        task()
        print("Done\n")


if __name__ == "__main__":
    main()
