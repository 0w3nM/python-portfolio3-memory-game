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

if user_sequence == numbers:
    print("Correct!")
else:
    print("Incorrect! Answer is :", numbers)
