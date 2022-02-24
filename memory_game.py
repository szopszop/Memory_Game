import os, random, string

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

CURREMT_COL = 10
CURREMT_ROW = 5

def empty_board() -> list:
    board = [[0]*CURREMT_COL for _ in range(CURREMT_ROW)]
    return board

def print_board(game_board: list, the_answear_board: list):

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
                    print(the_answear_board[i][j], end=' ')   
        print()   




def answear_board() -> list:
    letter_range = int(CURREMT_COL * CURREMT_ROW / 2)
    alphabet2 = list(string.ascii_uppercase[:letter_range] ) *2
    random.shuffle(alphabet2)

    the_answear_board = [[0]* CURREMT_COL for i in range(CURREMT_ROW)]
    
    for col in range(CURREMT_ROW):
        for row in range(CURREMT_COL):
            the_answear_board[col][row] = alphabet2[col * CURREMT_COL + row]

    return  the_answear_board

def game_board() -> list:
    game_board = [[0]* CURREMT_COL for i in range(CURREMT_ROW)]
    return game_board




def user_move(game_board) -> tuple:
    allowed_col = string.ascii_uppercase[0:CURREMT_COL]
    allowed_row = []
    for i in range(CURREMT_ROW):
        allowed_row.append(i+1)
    print('ALLOWED:',allowed_row, allowed_col)
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
        if user_input[0] in allowed_row and int(user_input[1:]) in allowed_col:
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


# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    console_clear()
    current_game_board = game_board()
    the_answear_board = answear_board()

    for line in current_game_board:
        print(line)
    for line in the_answear_board:
        print(line)


    print_board(current_game_board, the_answear_board)


    row1, col1, row2, col2 = -1, -1, -1, -1

    while True:
        print('Your first move: ')
        row1, col1 = user_move(current_game_board)
        current_game_board[row1][col1] = 1
        print_board(current_game_board, the_answear_board)

        print('Your second move: ')
        row2, col2 = user_move(current_game_board)
        current_game_board[row2][col2] = 1
        print_board(current_game_board, the_answear_board)

        if the_answear_board[row1][col1] == the_answear_board[row2][col2]:
            current_game_board[row1][col1] = 2
            current_game_board[row2][col2] = 2
        else:
            current_game_board[row1][col1] = 0
            current_game_board[row2][col2] = 0
        

        stop = input('\nPress enter after you memorize it.')
        console_clear()
        print_board(current_game_board, the_answear_board)





def main():
    game()
    #TODO LVL 


if __name__ == "__main__":
    main()