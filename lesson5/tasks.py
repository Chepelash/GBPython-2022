import os
import re
import random

def task1():
    DIGIT_NAME = "digit"
    DEGREE_NAME = "degree"
    OUT_FILENAME = "out.txt"

    def parse_polynomial(polynomial: str) -> list:
        pattern = r"(?P<digit>[+-]?\d+)(?:\*)?(?P<x>x)?(?:\^(?P<degree>[+-]?\d+)?)?"
        polynomial = str.replace(polynomial, " ", "")
        polynomial_iter = re.finditer(pattern, polynomial)
        result_list = []
        
        for entry in polynomial_iter:
            internal_dict = {}    
            if entry.group("x") is None:
                internal_dict[DEGREE_NAME] = 0
            else:
                if entry.group(DEGREE_NAME) is None:
                    internal_dict[DEGREE_NAME] = 1
                else:
                    internal_dict[DEGREE_NAME] = int(entry.group(DEGREE_NAME))
            internal_dict[DIGIT_NAME] = int(entry.group(DIGIT_NAME))
            result_list.append(internal_dict)

        return result_list
                

    path_input_1 = input("Enter a path to first file > ")
    path_input_2 = input("Enter a path to second file > ")
    if not os.path.isfile(path_input_1) or not os.path.isfile(path_input_2):
        print("Inputs were not files")
        return
    with open(path_input_1, 'r') as f:
        file_text_1 = f.readline()
    with open(path_input_2, 'r') as f:
        file_text_2 = f.readline()
    list_1 = parse_polynomial(file_text_1)
    list_2 = parse_polynomial(file_text_2)
    if len(list_1) > len(list_2):
        smaller_list = list_2
        bigger_list = list_1
    else:
        smaller_list = list_1
        bigger_list = list_2
    
    copy_of_smaller_list = smaller_list.copy()
    for element in smaller_list:
        for el in bigger_list:
            if element[DEGREE_NAME] == el[DEGREE_NAME]:
                el[DIGIT_NAME] += element[DIGIT_NAME]
                copy_of_smaller_list.remove(element)
                break
    if len(copy_of_smaller_list):
        bigger_list.extend(copy_of_smaller_list)
    bigger_list.sort(key=lambda x: x[DEGREE_NAME], reverse=True)
            
    with open(OUT_FILENAME, 'w') as f:
        for el in bigger_list:
            f.write(f"{el[DIGIT_NAME]:+}")
            if el[DEGREE_NAME] > 1:
                f.write(f"*x^{el[DEGREE_NAME]}")
            elif el[DEGREE_NAME] == 1:
                f.write("*x") 
    print(f"Result was written to {os.path.join(os.path.abspath(), OUT_FILENAME)}")    


def task2():
    pass
     


def task3():
    GAME_TYPES = ("pvp", "pve")
    PLAYER_NAME_1 = "player_1"
    PLAYER_NAME_2 = "player_2"
    MAX_CANDIES_AT_START = 101
    MAX_CANDIES_TO_TAKE = 28
    MAX_FAILED_INPUTS = 3
    
    def get_player_order(player_data_1: dict, player_data_2: dict) -> list:
        result = [player_data_1, player_data_2]
        random.shuffle(result)
        return result

    def bot_decision(number_of_candies: int) -> int:
        if number_of_candies > MAX_CANDIES_TO_TAKE:
            winning_number = number_of_candies % MAX_CANDIES_TO_TAKE - 1
            make_decision = lambda x: 1 if x < 1 else x
            return make_decision(winning_number)            
        else:
            return number_of_candies
        

    def human_decision() -> int:
        fail_cntr = 0
        while fail_cntr < MAX_FAILED_INPUTS:
            candies_taken_input = input("And you took > ")
            if candies_taken_input.lower() == 'q':
                return -1
            try:
                candies_taken = int(candies_taken_input)
            except ValueError:
                print("Wrong input")
                fail_cntr += 1
                continue
            if candies_taken > MAX_CANDIES_TO_TAKE:
                print(f"Max candies to take per turn = {MAX_CANDIES_TO_TAKE}")
                fail_cntr += 1
                continue
            elif candies_taken < 1:
                print("You cant take negative number of candies")
                fail_cntr += 1
                continue
            break
        if fail_cntr == MAX_FAILED_INPUTS:
            return -2
        
        return candies_taken            

    print("Candy game")
    game_type = input("Choose game type: vs player type 'pvp', vs bot - 'pve' > ")
    if game_type not in GAME_TYPES:
        print("Wrong input")
        return
    
    print("Game starts in ", end="")
    if game_type == 'pvp':
        pvp = True
        print("pvp mode")
    else:
        pvp = False
        print("pve mode")
    
    is_game_going = True
    number_of_candies = MAX_CANDIES_AT_START
    player_data_1 = {"name": PLAYER_NAME_1, "candies": 0, "bot": False}
    player_data_2 = {"name": PLAYER_NAME_2, "candies": 0, "bot": not pvp}
    player_list = get_player_order(player_data_1, player_data_2)
    print(f"First player is {player_list[0]['name']}")
    while is_game_going:
        for player in player_list:
            print(f"There are {number_of_candies}. {player['name']} can take up to {MAX_CANDIES_TO_TAKE}. Or 'q' to exit")
            if player["bot"]:
                result = bot_decision(number_of_candies)
                print(f"Bot took {result} candies...")
            else:
                result = human_decision()
                if result < 0:
                    if result == -2:
                        print("You failed at following instructions too many times")
                        return
                    elif result == -1:
                        print("Quitting...")
                        return
            if result > number_of_candies:
                print(f"You took only {number_of_candies} candies...")                
            number_of_candies -= result            
            if number_of_candies <= 0:
                victor = player
                is_game_going = False
                break
    print(f"{victor['name']} has won. Hurray")


def main():
    task_list = [task1, task2, task3]
    for task in task_list:
        print(f"{task.__name__}...")
        task()
        print("Done\n")


if __name__ == "__main__":
    main()
