from os import system, name 
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def display_board(board):
    clear()
    bright_yellow = "\033[0;93m"
    print(bright_yellow + '     |     |')
    print(bright_yellow + '7: ' + board[7] + ' |8: ' + board[8] + ' |9: ' + board[9])
    print(bright_yellow + '     |     |')
    print(bright_yellow + '------------------')
    print(bright_yellow + '     |     |')
    print(bright_yellow + '4: ' + board[4] + ' |5: ' + board[5] + ' |6: ' + board[6])
    print(bright_yellow + '     |     |')
    print(bright_yellow + '------------------')
    print(bright_yellow + '     |     |')
    print('1: ' + board[1] + ' |2: ' + board[2] + ' |3: ' + board[3])
    print(bright_yellow + '     |     |')
# user_choice()
bright_yellow = "\033[0;93m"
test_board = ['#','#','#','X','O','X','O','X','O','X']
display_board(test_board)

print(bright_yellow + "Hello world")