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
    

def main():
    task_list = [task1, task2]
    for task in task_list:
        print(f"{task.__name__}...")    
        task()
        print("Done\n")    


if __name__ == "__main__":
    main()
