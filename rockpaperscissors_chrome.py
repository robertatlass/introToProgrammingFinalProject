'''
Sources:
1) https://realpython.com/python-rock-paper-scissors/ 
2) https://codereview.stackexchange.com/questions/43024/use-if-else-elif-conditionals-to-write-a-basic-rock-paper-scissors-game
Questions: What does the f and /n do that is the only difference between my first thoughts and seconds thoughts
'''
#Imports Random Library
# import random

# Asks the player to pick their choice in the terminal
player1_choice = input("Player1: please Pick from rock, paper, or scissors (case sensitive):")
player2_choice = input (" Player2: please Pick from rock, paper, or scissors (case sensitive):")
# these are the choices the computer can pick from
possible_choices = ["rock", "paper", "scissors"]
# defines the function
def myfunc(possible_choices):
# Randomly picks from one of the possible_choices variable
    print(f"\n The player chose {player1_choice}, the computer chose {player2_choice}.\n")
# if the player choice and computer are the same this is what to print
    if player1_choice == player2_choice:
        print(f"Both of you selected {player1_choice}. That is lame! It's a tie!")
# All possible outcomes if the player chooses rock
    elif player1_choice == "rock":
        if player2_choice == "scissors":
            print("Rock crushes scissors! Player 1 wins! Nice Job! :)")
        else:
            print("Paper covers rock! Player 2 wins! You are a loser!")
# All possible outcomes if the player chooses paper           
    elif player1_choice == "paper":
        if player2_choice == "rock":
            print("Paper covers rock! Player 1 wins! Nice Job! :)")
        else:
            print("Scissors cuts paper! player 2 wins! You are a loser!.")
# All possible outcomes if the player chooses paper                 
    elif player1_choice == "scissors":
        if player2_choice == "paper":
            print("Scissors cuts paper! player 1 wins! Nice Job! :)")
        else:
            print("Rock crushes scissors! player 2 wins! You are a loser.")
myfunc(possible_choices)






'''
I AM NOT SURE WHY THE PRORGRAM GIVE INCORRECT STATEMENTS ON WHY THE PERSON OR COMPUTER WON THE GAME
# Import Random Library
import random
# Create Play Again Option
# Take Player Input
player_choice = input("Please Pick from Rock, Paper, or Scissors (case sensitive): ") 
player_choice == "Rock", 'Paper', 'Scissors'
#define the list
Computer_Choice = ['Rock', 'Paper', 'Scissors']
# Defines The Function
def myfunc(Computer_Choice): 
   print("The Computer Picked " + random.choice(Computer_Choice))    
#If Player and Computer Choices are the Same
   if player_choice == Computer_Choice:
      print("It is a Tie!")
   # If player choice is paper - All Combinations
   elif player_choice == "Paper":
      if Computer_Choice == "Scissors":
         print("Scissors Cut Paper, Computer Wins! YOU LOOSE HAHA!")
      else: 
         print("Paper Covers Rock, You Win!")
   # If Player choice is Rock - All Combinations
   elif player_choice == "Rock":
      if Computer_Choice == "Scissors":
         print("Rock Crushes Scissors, Computer Wins! YOU LOOSE HAHA!")
   else: 
         print("Paper Covers Rock, Computer Wins! YOU LOOSE HAHA!")
   # If player choice is Scissors - All Combinations      
   # elif player_choice == "Scissors":
if Computer_Choice == "Paper":
         print("Scissors Cut Paper, You Win!")   
else:
         print("Rock Crushes Scissors, Computer Wins! YOU LOOSE HAHA!")
# Computer Picks Rock Paper or Scissors   
myfunc(Computer_Choice)
'''