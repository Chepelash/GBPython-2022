
def task1():
    """
    Создайте программу для игры в "Крестики-нолики".
    """
    MIN_BOARD_SIZE = 3
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
                print(''.join("-" for _ in range(4*MIN_BOARD_SIZE)))                
    
    def human_decision(board: list) -> int:
        fail_cntr = 0
        while fail_cntr < MAX_FAILED_INPUTS:
            choice = input(f"Enter x and y separated by space (indexes from 1 to {len(board)}). Or 'q' to quit \n> ")
            if choice.lower() == 'q':
                return -1
            if not str.isdigit(choice):
                print("Wroing input")
                fail_cntr += 1
                continue
            choice = int(choice)

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

    def check_victory(board: list, symb_to_check: str, new_x: int, new_y: int) -> bool:
        #check left
        #check right
        #check up
        #check down
        #check NE
        #check NW
        #check SE
        #check SW
        return True
    
    print("tic-tac-toe game")
    board = [EMPTY_SYMBOL for _ in range(MIN_BOARD_SIZE*MIN_BOARD_SIZE)]
    
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
            board[choice] = symb
            if check_victory(board, symb):
                victor = symb
                is_game_going = False
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
