# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

# num= random.randrange(1, 10**3):03
num = 1111

while True:

    cows_bulls = ''
    guess = int(input('Guess the no'))

    nums_list = [i for i in str(num)]
    guess_list = [i for i in str(guess)]

    for i, j in zip(nums_list, guess_list):
        # print(f'{i} , {j}')
        if int(i) == int(j):
            cows_bulls += 'cows_'
        else:
            cows_bulls += 'bulls_'

    if 'bulls' not in cows_bulls:
        break
    print(f'{cows_bulls}')


print(f'you guessed right ')




