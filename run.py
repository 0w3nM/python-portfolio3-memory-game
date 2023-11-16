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

    global score
    
    if user_guess == number_to_guess:
        print("Congratulations! You guessed it right!")       
    else:
        print("Sorry, you guessed it wrong.")        
        
    if not user_guess.isdigit() or len(user_guess) != 5:
        print("Please Enter A 5-Digit Number")
        return False

    return user_guess == number_to_guess


def play_game():
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
        print("Thanks for Playing!")
        sys.exit()


def main():
    """
    Function that runs and finishes the game.
    """    
    score = play_game()
    if score >= 3:
        print(f"Congratulations! You matched {score} out of 5 numbers. You win!")
    else:
        print(f"Sorry, you matched {score} out of 5 numbers. You lost.")   
    game_restart()


if __name__ == "__main__":
    main()
