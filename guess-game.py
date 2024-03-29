
import random
import os
import art_guess_game

def guessgame():
    attemp =  0
    correct_answer = False
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        attemp += 5

    while correct_answer == False and attemp < 10:
        random_number = 1 #random.choice(numbers)
        print(f"You have {10 - attemp} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        
        if user_guess > random_number:
            print("Too High")
            attemp += 1
            if attemp < 10:
                print("Guess again.")
        elif user_guess < random_number:
            print("Too Low")
            attemp += 1
            if attemp < 10:
                print("Guess again.")
        elif user_guess == random_number:
            print(f"Correct ! The answer is {random_number}")
            correct_answer = True
    if attemp == 10:
        print("Sorry, youve ran out of guess, you lose")

os.system('cls')
print(art_guess_game.logo)
guessgame()
