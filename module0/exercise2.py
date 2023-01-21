import random
import numpy as np

guess = 0 
randomNumber = random.randrange( 1, 21 )

print( 'I have selected a random number between 1 and 20 inclusive. Guess my number.' )

# The while loop, if, and elif conditions are incorrect. Replace True with the correct
# relational expressions. 
while guess != randomNumber:
    # randomNumber = random.randrange( 1, 21 )
    guess = int( input( 'What is your guess? ' ) )

    if guess == randomNumber:
        print( 'You are correct!' )
    elif guess > randomNumber:
        if guess not in np.arange(1,21):
            print(f"{guess} is outside of the range. Try a different number between 1 and 20!")
        else:
            print( 'Incorrect -- your guess is too high.' )
    elif guess < randomNumber:
        if guess not in np.arange(1,21):
            print(f"{guess} is outside of the range. Try a different number between 1 and 20!")
        else:
            print( 'Incorrect -- your guess is too low.' )
    else:
        print("Hmm... I don't understand this input. Try again!")
    
    print( 'Game over!' )
    print( '###############' )