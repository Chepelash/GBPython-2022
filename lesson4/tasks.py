
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
    NUMBER_OF_GAMES_KEY = "numberOfGames"
    VICTORIES_KEY = "victories"
    LOSS_KEY = "loss"
    DRAW_KEY = "draw"
    SCORE_KEY = "score"

    def fill_score(game_result: int, team_name: str, result_dict: dict) -> dict:
        # victory
        if game_result == 1:
            if team_name in result_dict:
                result_dict[team_name][NUMBER_OF_GAMES_KEY] += 1
                result_dict[team_name][VICTORIES_KEY] += 1
                result_dict[team_name][SCORE_KEY] += 3
            else:
                result_dict[team_name] = {NUMBER_OF_GAMES_KEY: 1, VICTORIES_KEY:1, DRAW_KEY: 0, LOSS_KEY: 0, SCORE_KEY: 3}
        # loss
        elif game_result == -1:
            if team_name in result_dict:
                result_dict[team_name][NUMBER_OF_GAMES_KEY] += 1
                result_dict[team_name][LOSS_KEY] += 1
            else:
                result_dict[team_name] = {NUMBER_OF_GAMES_KEY: 1, VICTORIES_KEY:0, DRAW_KEY: 0, LOSS_KEY: 1, SCORE_KEY: 0}
        # draw
        elif game_result == 0:
            if team_name in result_dict:
                result_dict[team_name][NUMBER_OF_GAMES_KEY] += 1
                result_dict[team_name][DRAW_KEY] += 1
                result_dict[team_name][SCORE_KEY] += 1
            else:
                result_dict[team_name] = {NUMBER_OF_GAMES_KEY: 1, VICTORIES_KEY:0, DRAW_KEY: 1, LOSS_KEY: 0, SCORE_KEY: 1}
        return result_dict

    number_of_games_str = input("Enter number of games > ")
    try:
        number_of_games = int(number_of_games_str)
    except ValueError:
        print("Wrong input")
        return
    
    results = {}
    max_retries = 3
    for i in range(number_of_games):
        retry_cntr = 0
        while retry_cntr < max_retries:
            game_info_input = input(f"Enter game {i+1} > ")
            game_info = game_info_input.split(";")
            if len(game_info) != 4:
                print("Wrong input, try again")
                retry_cntr += 1
                continue
            team_name_1, goals_1, team_name_2, goals_2 = game_info
            try:
                goals_1 = int(goals_1)
                goals_2 = int(goals_2)
            except ValueError:
                print("Wrong score, try again")
                retry_cntr += 1
                continue
            break

        if retry_cntr == 3:
            print("Out of tries")
            return
        
        if goals_1 > goals_2:
            results = fill_score(1, team_name_1, results)
            results = fill_score(-1, team_name_2, results)
        elif goals_1 < goals_2:
            results = fill_score(1, team_name_2, results)
            results = fill_score(-1, team_name_1, results)
        else:
            results = fill_score(0, team_name_2, results)
            results = fill_score(0, team_name_1, results)
    
    for k, v in results.items():
        print(f"{k}: {v[NUMBER_OF_GAMES_KEY]} {v[VICTORIES_KEY]} {v[DRAW_KEY]} {v[LOSS_KEY]} {v[SCORE_KEY]}")


def main():
    task_list = [task1, task2, task3]
    for task in task_list:
        print(f"{task.__name__}...")
        task()
        print("Done\n")


if __name__ == "__main__":
    main()
