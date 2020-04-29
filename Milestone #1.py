#Function that prints out a board. Where each index 1-9 corresponds with a number on number pad.
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-+-+-")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-+-+-")
    print(board[1]+'|'+board[2]+'|'+board[3])
    
    
#Function that takes in player's input and assigns their marker as "X" or "O".

def player_input():
    marker = ''
    while marker != 'X' and marker !='O':
        marker = input("Player 1 please select your marker between X or O: ")

    player1 = marker
    if player1 == "X":
        player2 ="O"
    else:
        player2 ="X"

    return(player1, player2)
