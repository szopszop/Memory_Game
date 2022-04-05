import os, random, string

def game_board() -> list:
    game_board = [[0]* CURREMT_COL for i in range(CURREMT_ROW)]
    return game_board


def print_board(game_board: list, the_answer_board: list):
    print("    ", end='')
    for i in range(CURREMT_COL):
        print(chr(65+i), end=' ')
    print('\n')
    for i in range(CURREMT_ROW):
        print(str(i+1),' ', end=' ')
        for j in range(CURREMT_COL):
                if game_board[i][j]==0:
                    print("#", end=' ')
                if game_board[i][j]==1 or game_board[i][j]==2:
                    print(the_answer_board[i][j], end=' ')   
        print()   


def answer_board() -> list:
    letter_range = int(CURREMT_COL * CURREMT_ROW / 2)
    alphabet = list(string.ascii_uppercase[:letter_range] ) *2
    random.shuffle(alphabet)
    the_answer_board = [[0]* CURREMT_COL for i in range(CURREMT_ROW)]
    for col in range(CURREMT_ROW):
        for row in range(CURREMT_COL):
            the_answer_board[col][row] = alphabet[col * CURREMT_COL + row]
    return  the_answer_board


def user_move(game_board: list) -> tuple:
    allowed_col = string.ascii_uppercase[0:CURREMT_COL]
    allowed_row = []
    for i in range(CURREMT_ROW):
        allowed_row.append(i+1)
    row, col = -1, -1
    is_empty_flag = False
    is_valid_flag = False
    user_input = ''

    while not (is_valid_flag and is_empty_flag):
        is_empty_flag = False
        is_valid_flag = False
        user_input = input().upper()
        if len(user_input) not in [2,3]:
            print("Try again.")
            continue
        if user_input[0] in allowed_col and int(user_input[1:]) in allowed_row:
            is_valid_flag = True
        else:
            print("Try again.")
            continue 

        col = int(ord(user_input[0])-65)
        row = int(user_input[1:])-1 
        
        if game_board[row][col] == 0:
            is_empty_flag = True
        else:
            print('You already guessed that.')
            continue

        if is_empty_flag and is_valid_flag:
            return row, col


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def game_init():
    console_clear()
    current_game_board = game_board()
    the_answer_board = answer_board()
    """ TESTING """
    for line in current_game_board:
        print(line)
    for line in the_answer_board:
        print(line)
    print_board(current_game_board, the_answer_board)
    return current_game_board,the_answer_board


def game():
    current_game_board, the_answer_board = game_init()
    points = 0
    while True:
        print('Your first move: ')
        row1, col1 = user_move(current_game_board)
        current_game_board[row1][col1] = 1
        print_board(current_game_board, the_answer_board)

        print('Your second move: ')
        row2, col2 = user_move(current_game_board)
        current_game_board[row2][col2] = 1
        print_board(current_game_board, the_answer_board)

        if the_answer_board[row1][col1] == the_answer_board[row2][col2]:
            current_game_board[row1][col1] = 2
            current_game_board[row2][col2] = 2
            points += 1
        else:
            current_game_board[row1][col1] = 0
            current_game_board[row2][col2] = 0
        
        if has_won(points): break

        input('\nPress Enter after you memorize it.')
        console_clear()
        print_board(current_game_board, the_answer_board)


def choose_level():
    global CURREMT_COL
    global CURREMT_ROW
    user_input = input("Choose difficulty level(\"Easy\Medium\Hard\"): ").upper()
    if user_input == "EASY" or user_input.startswith("E"):
        CURREMT_COL = 5
        CURREMT_ROW = 4
    elif user_input == "MEDIUM" or user_input.startswith("M"):
        CURREMT_COL = 5
        CURREMT_ROW = 6
    elif user_input == "HARD" or user_input.startswith("H"):
        CURREMT_COL = 10
        CURREMT_ROW = 5


def has_won(points):
    if points == CURREMT_COL * CURREMT_ROW / 2:
        print('Congratz')
        play_again = input('Do you wanna play again? (Y/N').upper()
        if play_again == 'Y':
            main()
        else:
            exit()
    

def main():
    while True:
        print('\nWelcome to the Memory Game!')
        choose_level()
        game()


if __name__ == "__main__":
    main()