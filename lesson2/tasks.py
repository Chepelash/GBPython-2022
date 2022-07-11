def task1():
    """
    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    Пример:
    - 6782 -> 23
    - 0,56 -> 11
    """    
    input_number_string = input("Enter a real number > ")
    input_number_string = input_number_string.replace(",", ".")
    try:
        float(input_number_string)
    except ValueError:
        print("Wrong input")
        return
    
    sum = 0
    for symb in input_number_string:
        if symb == '.':
            continue
        sum += int(symb)
    print(f"- {input_number_string} -> {sum}")


def task2():
    """
    Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    Пример:
    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
    """
    n_number_str = input("Enter a number N > ")
    try:
        n_number = int(n_number_str)
    except ValueError:
        print("Wrong input")
        return
    
    print(f"N = {n_number_str} -> [", end="")
    res = 1
    for i in range(n_number):
        res *= i+1
        print(res, end="")
        if i < n_number-1:
            print(", ", end="")
        else:
            print("]")


def main():
    task_list = [task1, task2]
    for task in task_list:
        print(f"{task.__name__}...")
        task()
        print("Done\n")


if __name__ == "__main__":
    main()
