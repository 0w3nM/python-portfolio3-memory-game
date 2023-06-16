# Modules
from random import shuffle
import os
import sys
from time import sleep

# Users board
user_board = [[""] * 9 for i in range(9)]

# Counts the number of gueses user is limited to.
guess_limit = 0
# Counts how many answers were correct.
correct_guesses = 0
# Length of numbers shown.
sequence_length = 6
# Highest number that will be shown.
max_number = 9
# Numbers that are shown.
numbers = []


def rules():
    """
    Description of the game and its rules.
    """
    print("Welcome to the Memory Game! /n")
    print("The objective of this game is for you to try and guess the sequence")
    print("Fail more than 3 times and its GAME OVER!")
    

def print_board(board):
    """
    Function to print board
    """
    print('+') * 9
    row_number = 1


def random_numbers():
    """
    List of randomised numbers.
    """
    for sequence_index in range(sequence_length):
        random_numbers = randint(1, max_number)
        numbers.append(random_numbers)
    print("Guess the sequence", numbers)


def user_input(board):
    """
    Allows player to input guess
    of the sequence.
    """
    user_guess = int(input("What was the Sequence ?: "))

    
while guess_limit < 5:
    guess = int(input())
    guess_limit = + 1
    if guess == random_numbers:
        print("CORRECT !!")
    if guess != random_numbers:
        print("Incorrect!! Sequence is: ", random_numbers)
        break

while correct_guesses < 5:
    guess = int(input())
    correct_guesses = + 1
    if correct_guesses <= 3:
        print("YOU LOSE !!")
    if correct_guesses >= 3:
        print("YOU WIN!!")
        break


def play_game():
    """
    Function to start and play game.
    """
    # Adds the board for user.
    print_board(user_board)
    while True:
        print(random_numbers)
        print(user_input)
        if guess_limit == 5:
            print(guess_limit)
            print(correct_guesses)
            return cont_game()

def cont_game():
    """
    Allows the user to keep playing
    """
    user_board = [[""] * 9 for i in range(9)]
    print("Do you wish to continue playing?")
    answer = input("Y / N").upper()
    print("")
    while True:
        if answer == "Y":
            play_game()
        elif answer == "N":
            print("")
            print("Thanks for Playing!")
            sys.exit()




# Print statement showing the final resuilt of the game.
print("-") * 25
print(f"Your Total is {correct_guesses} out of {guess_limit}")