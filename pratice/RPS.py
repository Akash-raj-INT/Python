from random import random


user_input = input("enter a choice : rock, paper, scissors")
possible_action = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_action)

print(f"my choice {user_input} and computer choice {computer_action}")

if computer_action == rock or user_input==paper :
    print()
