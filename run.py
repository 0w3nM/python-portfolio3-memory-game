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
    print("Remember this number for 5 seconds: ", number_to_guess)
    time.sleep(5)
    os.system("clear")
    user_guess = input("Enter Guess: ")

    if user_guess == number_to_guess:
        print("Congratulations! You guessed it right!")
    else:
        print("Sorry, you guessed it wrong.")
    if not user_guess.isdigit() or len(user_guess) != 5:
        print("Please Enter A 5-Digit Number")
        return False

    return user_guess == number_to_guess


def valid_name():
    """
    Asks user for their name and returns it
    """
    while True:
        user_name = input("Enter Name: ")
        if user_name.isalpha():
            return user_name
        else:
            print("Invalid, Please Enter A Valid Name")


def play_game(user_name):
    score = 0
    guesses = 5
    for _ in range(guesses):
        if num_guess():
            score += 1
    return score


def game_restart():
    """
    Allows the user to keep playing
    """
    restart = input("Do you wish to continue playing? (y/n) ")
    if restart == "y":
        os.system('clear')
        main()
    else:
        sys.exit("Thanks for Playing!")


def main():
    """
    Function that runs and finishes the game.
    """
    user_name = valid_name()
    score = play_game(user_name)
    if score >= 3:
        print(f"Congratulations {user_name}! You Guessed {score} out of 5,
              You win!")
    else:
        print(f"Sorry {user_name}, You Guessed {score} Out Of 5, You Lost.")
    game_restart()


if __name__ == "__main__":
    main()
