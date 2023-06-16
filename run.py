# Modules
from random import shuffle
import os
import system
from time import sleep

# Counts the number of gueses user is limited to.
guess_limit = 0
# Counts how many answers were correct.
correct_guesses = 0


def rules():
    """
    Description of the game and its rules.
    """
    print("Welcome to the Memory Game! /n")
    print("The objective of this game is for you to try and guess the sequence")
    print("Fail more than 3 times and its GAME OVER!")
    

def random_list():
    sequence_length = 6
    low_number = 1
    max_number = 9
    random_list = random.shuffle(range(low_number, max_number),sequence_length)
    print(random_list)

print ("Guess the sequence: ", random_list)

def user_input(prompt):
    return input (prompt)

guess = user_input("Type the order of the numbers: ")
user_sequence = list(map(int, guess.split()))

if user_sequence == random_list:
    print("Correct!")
else:
    print("Incorrect! Answer is :", random_list)

while guess_limit < 5:
    guess = int(input())
    guess_limit =+ 1
    if guess == random_list:
        print("CORRECT !!")
    if guess != random_list:
        print ("Incorrect!! Sequence is: ", random_list)
        break

while correct_guesses < 5:
    guess = int(input())
    correct_guesses =+ 1
    if correct_guesses <= 3:
        print("YOU LOSE !!")
    if correct_guesses >= 3:
        print("YOU WIN!!")
        break

# Print statement showing the final resuilt of the game.
print(f"Your Total is {correct_guesses} out of {guess_limit}")