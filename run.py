# Modules
import random
import os
import sys
import time
from time import sleep


# Users board
user_board = [[""] * 4 for i in range(4)]

correct_guesses = 0
guess_limit = 0
my_sequence = [1, 2, 3, 4]


def rules():
    """
    Description of the game and its rules.
    """


print("Welcome to the Memory Game! /n")
print("The objective of this game is for")
print("you to try and guess the sequence.")
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


global my_sequence
count = 0
while count < len(my_sequence):
    my_sequence[count] = random.randint(1, 9)
    count = count = 1


def new_sequence():
    random.shuffle(my_sequence)
    random_numbers()
    print("Guess the sequence. They will disapper in 5 seconds")
    print(my_sequence, end="\r", flush=True)
    print(my_sequence)
    time.sleep(5)
    print('------', end="\r", flush=True)
    # sys.standout.flush()
    sys.stdout.write('\r')
    # print(" " * len(text), end="\r")
    os.system('cls')


def user_input(board):
    """
    Allows player to input guess
    of the sequence.
    """

    global guess_limit
    global random_number
    global correct_guesses

    guess_limit = 0
    correct_guesses = 0

    while guess_limit < 5:
        new_sequence()
        guess = input(
            f"What was the sequence"
            "space between, no commas)? :")
        guess_sequence = guess.split()
        input_index = len(guess_sequence) - 1
        while input_index >= 0:
            guess_sequence[input_index] = int(guess_sequence[input_index])
            input_index = input_index - 1

        print(guess_sequence)

        guess_limit = guess_limit + 1
        if guess_sequence == my_sequence:
            print("CORRECT !! ")
            correct_guesses = correct_guesses + 1
        if guess_sequence != my_sequence:
            print("Incorrect!! Sequecnce is:", my_sequence)

    
print("-" * 15)
print(f"Your Total is {correct_guesses} out of {guess_limit}")
print("-" * 15)

if correct_guesses < 3:
    print("YOU LOSE !!")
else:
    print("YOU WIN !!")


def play_game():
    """
    Function to start and play game.
    """

    print("-" * 15)
    # Adds rules function.
    print(rules)
    print("-") * 15
    # Adds the board for user.
    print_board(user_board)
    user_input(user_board)

    return cont_game()


def cont_game():
    """
    Allows the user to keep playing
    """


print_board(user_board)
print("Do you wish to continue playing?")
answer = input("Y / N").upper()
print("")
while True:
    if answer == "Y":
        play_game()
    if answer == "N":
        print("")
        print("Thanks for Playing!")
        sys.exit()


play_game()
