
def task1():
    """
    Создайте программу для игры в "Крестики-нолики".
    """
    MIN_BOARD_SIZE = 3
    GAME_SYMBOLS = "X", "O"
    EMPTY_SYMBOL = "_"
    MAX_FAILED_INPUTS = 3
    # BOARD_DICT = {"_":}

    def print_board(board: list):
        for line in board:
            print(line)
    
    def human_decision(board: list) -> tuple:
        fail_cntr = 0
        while fail_cntr < MAX_FAILED_INPUTS:
            coordinates = input(f"Enter x and y separated by space (indexes from 1 to {len(board)}). Or 'q' to quit \n> ")
            if coordinates.lower() == 'q':
                return -1, 0
            coord_list = coordinates.split(" ")
            if len(coord_list) != 2:
                print("Wrong input")
                fail_cntr += 1                
                continue
            x, y = coord_list
            if not str.isdigit(x) or not str.isdigit(y):
                print("Wrong input")
                fail_cntr += 1
                continue
            x, y = int(x)-1, int(y)-1
            if x < 0 or x > len(board)-1 or y < 0 or y > len(board)-1:
                print("Wrong index")
                fail_cntr += 1
                continue
            if board[y][x] != EMPTY_SYMBOL:
                print("Cell is not empty")
                fail_cntr += 1
                continue
            break
        if fail_cntr == MAX_FAILED_INPUTS:
            return -2, 0
        return x, y

    def check_victory(board: list) -> bool:
        return True
    
    print("tic-tac-toe game")
    board_size_input = input(f"Enter board size. Minimum size is {MIN_BOARD_SIZE} > ")
    if not str.isdigit(board_size_input):
        print("Wrong input")
        return
    board_size = int(board_size_input)
    if board_size < MIN_BOARD_SIZE:
        print("Size is too small")
        return

    board = [['_' for _ in range(board_size)] for _ in range(board_size)]
    
    is_game_going = True
    while is_game_going:
        for symb in GAME_SYMBOLS:
            print_board(board)
            print(f"{symb} player decision")
            x, y = human_decision(board)
            if x < 0:
                if x == -1:
                    print("Quitting...")
                    return
                elif x == -2:
                    print("You failed at following instructions too many times")
                    return
            board[y][x] = symb
            if check_victory(board):
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
