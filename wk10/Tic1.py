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
    green = "\033[0;32m"
    print(green  + '     |     |')
    print(green  + '7: ' + bright_yellow +  board[7] + green  +' |8: '+ bright_yellow  + board[8] + green  +' |9: '+ bright_yellow + board[9])
    print(green  + '     |     |')
    print(green  + '------------------')
    print(green  + '     |     |')
    print(green  + '4: ' + bright_yellow +  board[4] + green  +' |5: '+ bright_yellow  + board[5] + green  +' |6: '+ bright_yellow + board[6])
    print(green  + '     |     |')
    print(green  + '------------------')
    print(green  + '     |     |')
    print(green  + '1: ' + bright_yellow +  board[1] + green  +' |2: '+ bright_yellow  + board[2] + green  +' |3: '+ bright_yellow + board[3])
    print(green  + '     |     |')
# user_choice()

test_board = ['#','#','#','#','#','#','#','#','#','#']
display_board(test_board)

# print(bright_yellow + "Hello world")