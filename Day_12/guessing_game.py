"""Guessing Game"""

from random import randint
from art import logo

def check_answer(guess,answer):
    if guess> answer:
        print("Too high.")
    elif guess< answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")

answer = randint(1, 100)
print("Welcome to the Number Guessing Game! \n"
      "I'm thinking of a number between 1 and 100.")
print(logo)
guess = int(input("Make a guess:"))


