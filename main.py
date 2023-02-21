# a = 1
# def modify():
#     global a
#     a += 1
#     print(a)
# modify()

#####

# Day 12 Project: The Number Guessing Game

import random
import guessingGame

print(guessingGame.logo)

print("Welcome to The Number Guessing Game")

print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)

print(f"Pssst, the correct answer is {answer}")

difficultyLevel = input("Chose a difficulty level. Type 'e' for easy and 'h' for hard: ").lower()

if (difficultyLevel == 'e'):
    attempts = 10
elif (difficultyLevel == 'h'):
    attempts = 5

while (attempts > 0):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if (guess < answer):
        print("Too low.")
    elif (guess > answer):
        print("Too high.")
    elif (guess == answer):
        print(f"You got it! The answer was {guess}.")
        break
    attempts -= 1

if (attempts == 0):
    print("You have run out of guesses, you lose!")








