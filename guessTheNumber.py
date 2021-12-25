import random
from guessTheNumber_logo import logo

print(logo)

print("Welcome to the Number guessing game")
print('I\'m thinking of a number between 1 and 100.')

computerGuess = random.randint(1, 100)

difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

while difficulty not in ['easy', 'hard']:
    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    
if difficulty == 'easy':
    numTries = 10
else:
    numTries = 5
print(f'You have {numTries} attempts remaining to guess the number.')

isGameOver = False

def guessChecker(guess):
        
    global isGameOver, numTries
    
    if guess == computerGuess:
        isGameOver = not isGameOver
        print(f'You got it! The answer was {userGuess}')
    else:
        if guess > computerGuess:
            print('Too high')
        else:
            print('Too low')
            numTries -= 1
            if numTries == 0:
                isGameOver = not isGameOver
        if not isGameOver:
            print(f'Guess again.\nYou have {numTries} attempts remaining to guess the number.')
        else:
            print('You have no more attempts left. You lose.')


while not isGameOver:
    userGuess = int(input('Make a guess: '))
    guessChecker(userGuess)
    
    
    
    
    