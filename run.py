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


while guess_limit < 5:
    new_sequence()
    guess = input(
        f"What was the sequence"
        "space between, no commas)? :")
    guess_limit = guess_limit + 1

# join together the int list
joined = "".join([str(x) for x in my_sequence])

# check if the guess is the same as the joined list
if joined == guess:
    correct_guesses = correct_guesses + 1
    print("CORRECT !! ")
else:
    print("INCORRECT !! Sequence is:", my_sequence)

# isdigit check
user_input = ''

x = user_input.isdigit()

print(x)


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
