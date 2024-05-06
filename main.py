# imports
import random
from enum import Enum

# def get_choices():
# this function takes a user input and a random computer selection value
# and returns both choices
def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}. Computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock. You loose."
        else:
            return "Rock smashes scissors. You win!"  
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper. You loose."
        else:
            return "Paper covers rock. You win!" 
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors. You loose."
        else:
            return "Scissors cuts paper. You win!"  
    else:
        return "Error. Wrong choice!"

results = get_choices()
print(check_win(results["player"], results["computer"]))