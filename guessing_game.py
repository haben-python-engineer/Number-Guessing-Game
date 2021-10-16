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

    random_number = random.randint(1, 10)
    attempts = 1
    while True:
        try:
            guess = int(input('Take a shot and guess the mystery number. It\'s between 1 and 10: '))
            print('')
            if guess > 10 or guess < 1:
                raise ValueError(f'{guess} is not within the 1-10 range')
        except ValueError as e:
            print(f'Oh no! That is an invalid value ({e})')
        else:
            if guess > random_number:
                print('Oops! That guess is too high')
                attempts += 1
                continue
            elif guess < random_number:
                print('Oops! That guess is too low')
                attempts += 1
                continue
            elif guess == random_number:
                print(f'You solved the mystery! It took you {attempts} tries')
                random_number = random.randint(1, 10)
                play_again = input('Would you like to play again? (Yes/No): ')
                if play_again.lower() == 'yes':
                   continue
                elif play_again.lower() == 'no':
                    print('Thanks for playing! Bye for now.')
                    break












# Kick off the program by calling the start_game function.
start_game()