# Modules
import random
import os
import sys
import time
from time import sleep


def rules():
    """
    Description of the game and its rules.
    """


print("Welcome to the Memory Game!")
print("The objective of this game is for")
print("you to try and guess the sequence.")
print("Fail more than 3 times and its GAME OVER!")


def random_numbers():
    """
    List of randomised numbers.
    """


global my_sequence
my_sequence = [1, 2, 3, 4]
count = 0
while count < len(my_sequence):
    my_sequence[count] = random.randint(1, 9)
    count = count = 1


def new_sequence():
    random.shuffle(my_sequence)
    random_numbers()
    print("Guess the sequence. They will disapper in 5 seconds")
    time.sleep(5)
    os.system('clear')   
    print(my_sequence)

    vaidate_data(my_sequence)


def vailidate_data(guesses):
    """
    Function checks inputs are valid
    """
    try:
        [int(value) for value in guesses]
        if len(guesses) != 4:
            raise ValueError(
                f"Only 4 values are required, you gave {len(gueses)}"
            )
    except ValueError as e:
        print('f Invalid !: {e}, Enter 4 Digits.')


def user_input():
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
    
    return cont_game()


def cont_game():
    """
    Allows the user to keep playing
    """


print("Do you wish to continue playing?")
answer = input("Y / N")
print("")
while True:
    if answer == "Y":
        play_game()
    if answer == "N":
        print("")
        print("Thanks for Playing!")
        sys.exit()

play_game()
