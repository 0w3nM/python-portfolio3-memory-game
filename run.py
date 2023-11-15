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
print("-" * 46)
print("Welcome to the Memory Game!")
print("The objective of this game is for")
print("you to try and guess the sequence.")
print("Fail more than 3 times and its GAME OVER!")
print("-" * 46)


def random_number():
    """
    List of randomised numbers.
    """
    return str(random.randint(10000, 99999))


def num_guess():
    """
    Allows player to see the sequence
    and then input a guess of the sequence.
    """
    number_to_guess = random_number()
    print("Remember this sequence for 5 seconds: ", number_to_guess)
    time.sleep(5)
    os.system("clear")
    user_guess = input("Enter Guess: ")

    if not user_guess.isdigit() or len(user_guess) !=5:
        print("Please Enter A 5-Digit Number")
        return num_guess()
    else:
        return user_guess


def play_game():
    """
    Function to start and play game.
    """
    score = 0
    guesses = 5
    for _ in range(guesses):
        if num_guess():
            score += 1
    return score
    


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
