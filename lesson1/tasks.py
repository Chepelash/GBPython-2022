def task1():
    """
    Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    Пример:
    - 6 -> да
    - 7 -> да
    - 1 -> нет
    """
    try:
        day_number = int(input("Enter number of a day in a week > "))
    except ValueError:
        print("Value must be an integer")
        return
    
    if day_number < 1 or day_number > 7:
        print("Value must be in between 1 and 7 included")
        return
    
    print(f"- {day_number} -> ", end='')
    if day_number < 6:
        print("no")
    else:
        print("yes")
    

def task2():
    """
    изучить понятие Предкатов.
    """
    def is_there_something(input:str) -> bool:
        return bool(input)
    
    something = input("Will you enter something? > ")
    if(is_there_something(something)):
        print("You did")
    else:
        print("You did not")
    

def task3():
    """
    3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
    в которой находится эта точка (или на какой оси она находится).
    *Пример:*
    - x=34; y=-30 -> 4
    - x=2; y=4-> 1
    - x=-34; y=-30 -> 3
    """
    input_string = input("Enter x and y  separated by a space > ")    
    try:
        x, y = map(int, input_string.split(" "))
    except ValueError:
        print("Wrong input")
        return
    
    if x == 0 or y == 0:
        print("x and y must not be zero")
        return
    
    print(f"x = {x}; y = {y} -> ", end="")
    if y > 0:
        if x > 0:
            print(1)
        else:
            print(2)
    else:
        if x > 0:
            print(4)
        else:
            print(3)


def main():
    task_list = [task1, task2, task3]
    for task in task_list:
        print(f"{task.__name__}...")    
        task()
        print("Done\n")    


if __name__ == "__main__":
    main()
