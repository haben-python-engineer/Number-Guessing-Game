"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    print('_' * 55)
    print('Welcome! Test your skills and guess the mystery number!')
    print('_' * 55)

    mystery_number = random.randint(1, 10)
    attempts = 1
    print(mystery_number)
    while True:
        try:
            guess = int(input('Take a shot and guess the mystery number. It\'s between 1 and 10: '))
        except ValueError:
            print('Oh no! That is an invalid value. Please try again')
        else:
            if guess > 10 or guess < 1:
                print('Number is outside of the ranges 1-10')
                print('This will not be counted as an attempt')
            elif guess > mystery_number:
                print('Oops! That guess is too high')
                attempts += 1
            elif guess < mystery_number:
                print('Oops! That guess is too low')
                attempts += 1
            else:
                if attempts == 1:
                    print(f'You solved the mystery! It took you only {attempts} try awesome!')
                else:
                    print(f'You solved the mystery! It took you {attempts} tries')
                guess = input('Would you like to play again? (Yes/No): ')
                if guess.lower() == 'yes':
                    print(f'The current HIGHSCORE(Least amount of attempts taken to guess the number) is ---> {attempts}')
                    mystery_number = random.randint(1, 10)
                    attempts = 1
                    print(mystery_number)
                    continue
                elif guess.lower() == 'no':
                    print('Thanks for playing! See you soon!')
                    break





# Kick off the program by calling the start_game function.
start_game()