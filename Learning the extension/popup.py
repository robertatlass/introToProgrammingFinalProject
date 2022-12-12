#popup.py
from browser import document, prompt
import random

# -------------------------------------------- BEGIN ROCK PAPER SCISSORS --------------------------------------------------------
# Asks the player to pick their choice in the terminal
player_choice = input("Please Pick from rock, paper, or scissors (case sensitive):")
# these are the choices the computer can pick from
possible_choices = ["rock", "paper", "scissors"]
# defines the function
def myfunc(possible_choices):
# Randomly picks from one of the possible_choices variable
    computer_choice = random.choice(possible_choices)
    print(f"\n The player chose {player_choice}, the computer chose {computer_choice}.\n")
# if the player choice and computer are the same this is what to print
    if player_choice == computer_choice:
        print(f"Both of you selected {player_choice}. That is lame! It's a tie!")
# All possible outcomes if the player chooses rock
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock crushes scissors! You win! Nice Job! :)")
        else:
            print("Paper covers rock! Computer Wins! You are a loser!")
# All possible outcomes if the player chooses paper           
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win! Nice Job! :)")
        else:
            print("Scissors cuts paper! Computer Wins! You are a loser!.")
# All possible outcomes if the player chooses paper                 
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win! Nice Job! :)")
        else:
            print("Rock crushes scissors! Computer Wins! You are a loser.")
myfunc(possible_choices)
