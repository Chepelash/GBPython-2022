
def task1():
    """
    Создайте программу для игры в "Крестики-нолики".
    """
    MIN_BOARD_SIZE = 3
    BOARD_SIZE = MIN_BOARD_SIZE * MIN_BOARD_SIZE
    GAME_SYMBOLS = "X", "O"
    EMPTY_SYMBOL = "-"
    MAX_FAILED_INPUTS = 3

    def print_board(board: list):
        for i in range(len(board)):
            print(f" {board[i]} ", end="")
            if (i+1) % MIN_BOARD_SIZE > 0:
                print('|', end="")
            else:
                print()
                if i+1 < len(board):
                    print(''.join("-" for _ in range(4*MIN_BOARD_SIZE)))
                else:
                    print()
    
    def human_decision(board: list) -> int:
        fail_cntr = 0
        while fail_cntr < MAX_FAILED_INPUTS:
            choice = input(f"Enter an index from 1 to {len(board)}. Or 'q' to quit \n> ")
            if choice.lower() == 'q':
                return -1
            if not str.isdigit(choice):
                print("Wroing input")
                fail_cntr += 1
                continue
            choice = int(choice) - 1

            if choice < 0 or choice > len(board)-1:
                print("Wrong index")
                fail_cntr += 1
                continue
            if board[choice] != EMPTY_SYMBOL:
                print("Cell is not empty")
                fail_cntr += 1
                continue
            break
        if fail_cntr == MAX_FAILED_INPUTS:
            return -2
        return choice

    def check_victory(player_choices: list) -> bool:
        victory_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combination in victory_list: 
            if all(el in player_choices for el in combination):
                # Return True if any winning combination is satisfied 
                return True
        return False
    
    def check_tie(players: dict) -> bool:
        BOARD_SIZE
        cntr = 0
        for key in list(players):
            cntr += len(players[key])
        if cntr == BOARD_SIZE:
            return True
        return False


    print("tic-tac-toe game")
    print("Board indexes go like this")
    print_board([i+1 for i in range(MIN_BOARD_SIZE*MIN_BOARD_SIZE)])
    board = [EMPTY_SYMBOL for _ in range(MIN_BOARD_SIZE*MIN_BOARD_SIZE)]
    
    print("Starting...")
    players = {GAME_SYMBOLS[0]: [], GAME_SYMBOLS[1]: []}
    is_game_going = True
    while is_game_going:
        for symb in GAME_SYMBOLS:
            print_board(board)
            print(f"{symb} player decision")
            choice = human_decision(board)
            if choice < 0:
                if choice == -1:
                    print("Quitting...")
                    return
                elif choice == -2:
                    print("You failed at following instructions too many times")
                    return
            players[symb].append(choice)
            board[choice] = symb
            if check_victory(players[symb]):
                victor = symb
                is_game_going = False
                break
            if check_tie(players):
                is_game_going = False
                victor = "frendship"
                break
    print_board(board)
    print(f"Victor {victor} symbol gamer, hooray")




def task2():
    """
    Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный. 
    """
    equation = input("Enter your equation > ")
    try:
        print(f"{equation} => {eval(equation)}")
    except Exception:
        print("wrong equation")
     


def task3():
    """
    Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
    Входные и выходные данные хранятся в отдельных текстовых файлах.
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
