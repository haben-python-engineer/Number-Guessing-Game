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
    print('{}\nWelcome! Test your skills and guess the mystery number!\n{}'.format('_'*55,'_'*55))
    random_number = random.randint(1, 10)
    attempts = 1
    highscore = []
    while True:
        try:
            guess = int(input('Take a shot and guess the mystery number. It\'s between 1 and 10: \n>>> '))
            if guess < 1 or guess > 10:
                raise ValueError('Guess is not within the range of 1 and 10')
        except ValueError as error:
            print(f'Oh no! Ran into an error. ({error})')
        else:
            if guess > 10 or guess < 1:
                print('Over range')
            elif guess > random_number:
                print('Oops! That guess is too high')
                attempts += 1
                continue
            elif guess < random_number:
                print('Oops! That guess is too low')
                attempts += 1
                continue
            elif guess == random_number:
                print(f'You solved the mystery! It took you {attempts} tries')
                highscore.append(attempts)
                random_number = random.randint(1, 10)
                attempts = 1
                play_again = input('Want to play again?: ').upper()
                while play_again not in ['YES', 'NO']:
                    play_again = input('Please select either Yes OR No too continue: ').upper()
                else:
                    if play_again == 'YES':
                        print(f'\nLast HIGHSCORE was {min(highscore)}\n')
                        guess
                    else:
                        print('Thanks for playing! See you next time!')
                        break












# Kick off the program by calling the start_game function.
start_game()