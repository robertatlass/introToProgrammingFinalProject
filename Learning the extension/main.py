"""
Project Overview:
My Chrome extension is a rock paper scissors game. In this game the player inputs their choice of: "rock, paper, or scisscors." 
Then the computer picks from "rock, paper, or scisscors," at this point the computer and player choices are evaluated through 
a series of if statements. After the evaluation the winner is determined and the appropriate message is printed. 


The Chrome extension uses the Brython transpiler to take the rock paper scirssors game that is written in python 
and convert it into javascript so that it is available for web use
"""

# Disclaimer: The file GitHub commit history is located in the main.py file that is not in this folder. I copy and pasted all of this from my other main.py where I edited everything

# ROBERT ATLASS

# Sources:
    # https://www.youtube.com/watch?v=0n809nd4Zu4
    # https://www.youtube.com/watch?v=uV4L-wcnK3Y
    # https://support.google.com/chrome/a/answer/2714278?hl=en
    # https://developer.chrome.com/docs/extensions/mv3/getstarted/extensions-101/#building
    # https://pythonspot.com/create-a-chrome-plugin-with-python/
    # https://www.reddit.com/r/learnpython/comments/oi6wk8/creating_a_chrome_extension_with_python/
    # https://realpython.com/brython-python-in-browser/#creating-google-chrome-extensions
    # https://www.extension.ninja/blog/post/solved-permission-is-unknown-or-url-pattern-is-malformed/
    # https://pypi.org/project/rapydscript/
    # https://medium.com/swlh/sick-of-javascript-just-use-browser-python-4b9679efe08b
    # https://github.com/yakkomajuri/brython-snake
    # https://developer.chrome.com/docs/extensions/mv3/manifest/
    # https://www.w3schools.com/tags/att_input_src.asp#:~:text=Definition%20and%20Usage,type%3D%22image%22%3E%20.
    # https://github.com/atsepkov/RapydScript
    # https://stackoverflow.com/questions/42754611/creating-and-access-a-settings-class-from-the-main-file-in-python
    # https://www.youtube.com/watch?v=salY_Sm6mv4
    # https://www.youtube.com/watch?v=0n809nd4Zu4&t=4s
    # https://developer.chrome.com/docs/extensions/mv3/mv3-migration/
    # https://www.reddit.com/r/Python/comments/pvhrvg/brython/
    # https://bobbyhadz.com/blog/python-no-module-named-selenium#:~:text=The%20Python%20%22ModuleNotFoundError%3A%20No%20module,the%20pip%20install%20selenium%20command.
    # https://chromedriver.chromium.org/downloads
    # https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver
    # https://www.youtube.com/watch?v=zFZrkCIc2Oc

# ---------------------------------------------------- Beginning of Code ---------------------------------------------------------

# import library
import random

# ----------------------------------------- Rock Paper Scissors Code--------------------------------------------------------------
# defines the function
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
        yourmid = input("admit you failed by typing... I AM WEAK AND CAN'T WIN!")
# All possible outcomes if the player chooses rock
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock crushes scissors! You win! Nice Job! :)")
        else:
            print("Paper covers rock! Computer Wins! You are a loser!")
            yousuck1 = input("admit you failed by typing... I SUCK REALLY BADLY")
# All possible outcomes if the player chooses paper           
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win! Nice Job! :)")
        else:
            print("Scissors cuts paper! Computer Wins! You are a loser!.")
            yousuck2 = input("admit you failed by typing... I SUCK REALLY BADLY")
# All possible outcomes if the player chooses paper                 
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win! Nice Job! :)")
        else:
            print("Rock crushes scissors! Computer Wins! You are a loser.")
            yousuck3 = input("admit you failed by typing... I SUCK REALLY BADLY")
myfunc(possible_choices)