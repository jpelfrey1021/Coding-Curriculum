######################show board#########################
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])


#####################who is x and o######################
def player_input():
    marker = ''
    
    #keep asking player 1 to choose x or o
    while marker != 'X' and marker !='O':
        marker = input("Player 1, choose 'X' or 'O': ").upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O', 'X')


##################who goes first#######################
import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'


###############which space they are paying##############
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Select next position 1 through 9: "))
        
    return position

#is space emptty?#
def space_check(board, position):
    
    return board[position] == " "

#place the marker#
def place_marker(board, marker, position):
    board[position] = marker


#########################did someone win?###############
def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or 
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or 
    (board[1]==board[4]==board[7]==mark) or 
    (board[2]==board[5]==board[8]==mark) or 
    (board[3]==board[6]==board[9]==mark) or 
    (board[3]==board[5]==board[7]==mark) or 
    (board[1]==board[5]==board[9]==mark))


###################is there a tie#####################
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    #board is full
    return True


################replay?#####################
def replay():
    input("would you like to play again? enter 'Y' or 'N':").lower().startswith('y')




###################all together for the game############

print('Welcome to Tic Tac Toe!')

while True:

#start new game
    
    #board
    the_board = [' ']*10
    
    #choose markers
    player1_marker, player2_marker = player_input()
    
    #who goes first
    turn = choose_first()
    print(turn + " will go first.")
    
    play_game = input('Ready to play? enter y or n: ')
    
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False
    
#gameplay
    while game_on:
        
        #player 1 turn
        if turn == 'Player 1':
            
            #show the board
            display_board(the_board)
            
            #choose a position
            position = player_choice(the_board)
            
            #place the marker
            place_marker(the_board, player1_marker, position)
            
            #check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won")
                game_on = False
            
            #check if tie
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game")
                    game_on = False
                
                #no tie/win = next players turn
                else: turn = "Player 2"
        
        #player 2 turn
        else:
            #show the board
            display_board(the_board)
            
            #choose a position
            position = player_choice(the_board)
            
            #place the marker
            place_marker(the_board,player2_marker,position)
            
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has won")
                game_on = False
            
            #check if tie
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game")
                    game_on = False
                
                #no tie/win = next players turn
                else: turn = "Player 1"

    if not replay():
        break

