#Step 1 Function that prints out a board. Where each index 1-9 corresponds with a number on number pad.
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-+-+-")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-+-+-")
    print(board[1]+'|'+board[2]+'|'+board[3])
    
    
#Step 2, Function that takes in player's input and assigns their marker as "X" or "O".

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

#Step 3, Function that runs the place marker function and displays modified board

def place_marker(board, marker, position):
    
    board[position] = marker


#Step 4, Function that takes in board and a mark (X or O) and then check to see if that mark won.

def win_check(board, mark):
    
    return((board[7] == mark and board[8] == mark and board[9] == mark) or #accross the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or #accross the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

#Step 5, Function that uses random module to randomly decide which player goes first.

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"
    
#Step 6, Function that returns a boolean indicating whether a space on the board is free.

def space_check(board, position):
    
    return board[position] == " "

#Step 7, Function that checks if the board is full and returns a boolean.

def full_board_check(board):
    if " " in board:
        return False
    return True

#Step 8, Function that asks for a player's next position (as a number 1-9) and uses
#that function to check if it's a free position and then returns the position if it is. 

def player_choice(board):
    position = 0
    
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Please choose your next position between: 1-9 "))
        
    return position

#Step 9, Function that asks the player if they want to play again and returns a boolean
#True if they do or else False.

def replay():
    return input ("Would you like to play again? ").upper().startswith("Y")

