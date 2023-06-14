# Modules
import random
import os
from time import sleep

# How many numbers appear to the user.
sequence_length = 5
# How high the numbers shown will go upto.
max_number = 9


def rules():
    """
    Description of the game and its rules.
    """
    print("Welcome to the Memory Game! /n")
    print("The objective of this game is for you to try and guess the sequence")
    print("Fail more than 3 times and its GAME OVER!")

numbers = []


for sequence_index in range(sequence_length):
    random_number = random.randint(1, max_number)
    numbers.append(random_number)

print("Guess the sequence!: ", numbers)
print("Your screen will be cleared in 5 seconds...")
sleep(5)
os.system("clear")

guess = input("Type the order of the numbers: ")
guessed_sequence = list(map(int, guess.split()))

if guessed_sequence == numbers:
    print("Correct!")
else:
    print("Incorrect! Answer is :", numbers)
