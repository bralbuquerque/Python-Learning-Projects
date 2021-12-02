"""
Tic-Tac-Toe Game
-2 players should be able to play the game (both sitting at the same computer)
-The board should be printed out every time a player makes a move
-You should be able to accept input of the player position and then place a symbol on the board
"""

#Imports
import random

#Initialization
#Define possible tokens
tokens = ['X', 'O']


# Keep playing Tic-Tac-Toe flag
tic_tac_toe = True

#Functions
#Define function to print board with current configuration
def print_board(board_configuration):
    print(f'     |     |     ')
    print(f'  {board_config[0]}  |  {board_config[1]}  |  {board_config[2]}  ')
    print(f'_____|_____|_____')
    print(f'     |     |     ')
    print(f'  {board_config[3]}  |  {board_config[4]}  |  {board_config[5]}  ')
    print(f'_____|_____|_____')
    print(f'     |     |     ')
    print(f'  {board_config[6]}  |  {board_config[7]}  |  {board_config[8]}  ')
    print(f'     |     |     ')

#Define function that get player and wanted position and changes the board configuration
def play(token, pos, board_configuration):
    board_configuration[pos - 1] = token
    return board_configuration

#Define function to check if board is full
def check_full(board_configuration):
    for k in range(len(board_configuration)):
        flag = True
        if board_configuration[k] in list(range(1,10)):
           flag = False
           continue
        else:
            continue
    return flag


#Define function to check if any player won
def check_win(board_configuration):
    return ((board_configuration[0] == board_configuration[1] == board_configuration[2]) or # Across Top
            (board_configuration[3] == board_configuration[4] == board_configuration[5]) or # Across Middle
            (board_configuration[6] == board_configuration[7] == board_configuration[8]) or # Across Bottom
            (board_configuration[0] == board_configuration[3] == board_configuration[6]) or # Down Left
            (board_configuration[1] == board_configuration[4] == board_configuration[7]) or # Down Middle
            (board_configuration[2] == board_configuration[5] == board_configuration[8]) or # Down Right
            (board_configuration[0] == board_configuration[4] == board_configuration[8]) or # Diagonal 1
            (board_configuration[2] == board_configuration[4] == board_configuration[6]))   # Diagonal 2

# GAME LOGIC
# Initial Setup
# Choose player 1 name and token, repeat for player 2
player1_name = input('Player 1: Insert your name: ')

# Validate player 1 token and player 2
while True:
    player1_token = input('Player 1: Select your token (X/O): ')
    if player1_token in tokens:
        tokens.remove(player1_token)
        break
    else:
        pass
player2_name = input('Player 2: Insert your name: ')
player2_token = tokens[0]

# While loop to keep playing Tic-Tac-Toe while players want
while tic_tac_toe:

    # Define initial board configuration (empty)
    board_config = list(range(1,10))
    game_on = True

    # Play counter
    i = 1

    # Print a  welcome message to the screen
    print('***************************************************************************************')
    print('*                                                                                     *')
    print('*                            Welcome to Tic-Tac-Toe                                   *')
    print('*                                                                                     *')
    print('***************************************************************************************')
    print('\n\n')
    # GAME SETUP

    # Select randomly who is playing first
    first_player = random.randint(1, 2)
    if first_player == 1:
        print(f'{player1_name} will go first!!!')
        names = [player1_name, player2_name]
        tokens = [player1_token, player2_token]
    else:
        print(f' {player2_name} will go first!!!')
        names = [player2_name, player1_name]
        tokens = [player2_token, player1_token]
    # While loop to keep game on while board still has open positions and no player won
    while game_on:

        # Show current board
        print_board(board_config)
        # Ask player for a position and check if position is avaliable
        if i % 2 != 0:
            player = names [0]
            token = tokens[0]
        else:
            player = names[1]
            token = tokens[1]

        while True:
            pos = int(input(f'{player}: Select the desired position for your token: '))
            if pos in board_config and pos in list(range(1,10)):
                break
            else:
                print('Invalid Position')

        # Place token on board and show board
        board_config = play(token, pos, board_config)

            # Check winning configuration
        win = check_win(board_config)
        if win:
            print_board(board_config)
            print(f'{player} wins!!!')    
            game_on = False
            continue
        else:
            i += 1


        # Check full board
        full = check_full(board_config)
        if full:
            print('Game is a draw!!!')
            break
        else:
            pass

    # Ask if players want to play again
    while True:
        keep_playing = input('Do you want to keep playing Tic-Tac-Toe? (y/n)')
        if keep_playing == 'y':
            break
        elif keep_playing == 'n':
            tic_tac_toe = False
            print('Thank you for playing!!!')
            break
        else:
            pass






