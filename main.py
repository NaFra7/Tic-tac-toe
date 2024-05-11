import random
import time
import os
from game_manager import GameManager

game_over = False

Player_1 = {"Symbol": "X", "Moves": []}
Player_2 = {"Symbol": "O", "Moves": []}
Computer = {"Symbol": "O", "Moves": []}

game = GameManager()

#  Add game mode / computer opponent?
# mode_selected = input("Please choose either A: 2 Players or B: Computer Opponent (Type A or B): ")
#     if mode_selected == "A":
#         player_list = [Player_1, Player_2]
#     else:
#         player_list = [Player_1, Computer]
#     for player in player_list:
#         current_player = player_list[player]

game.show_board()

while not game_over:
    player1_choice = 0
    player2_choice = 0
    while player1_choice < 1 or player1_choice > 9:
        try:
            player1_choice = int(input("PLAYER 1: Please enter an available number on the board: "))
            if player1_choice < 1 or player1_choice > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            Player_1["Moves"] += str(player1_choice)
            game.update_board(str(player1_choice), Player_1)
        except ValueError:
            print("Invalid input. Please try again.")
    if game.check_for_winner(Player_1):
        print("Player 1 wins!")
        break
    elif len(Player_1["Moves"]) == 5 and len(Player_2["Moves"]) == 4:
        print("It's a Draw!")
        break

    while player2_choice < 1 or player2_choice > 9:
        try:
            player2_choice = int(input("PLAYER 2: Please enter an available number on the board: "))
            if player2_choice < 1 or player2_choice > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            Player_2["Moves"] += str(player2_choice)
            game.update_board(str(player2_choice), Player_2)

        except ValueError:
            print("Invalid input. Please try again.")
    if game.check_for_winner(Player_2):
        print("Player 2 wins!")
        break
