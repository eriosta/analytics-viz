import random
import numpy as np

print( 'I have selected a random number between 1 and 20 inclusive. Guess my number.' )

# The while loop, if, and elif conditions are incorrect. Replace True with the correct
# relational expressions. 
while True:
    randomNumber = random.randrange( 1, 21 )
    guess = int( input( 'What is your guess? ' ) )

    if guess == randomNumber:
        print( 'You are correct!' )
    elif guess > randomNumber:
        if guess is not np.arange(1,21):
            print(f"{guess} is outside of the range. Try a different number next time!")
        else:
            print( 'Incorrect -- your guess is too high.' )
    elif guess < randomNumber:
        if guess is not np.arange(1,21):
            print(f"{guess} is outside of the range. Try a different number next time!")
        else:
            print( 'Incorrect -- your guess is too low.' )
    else:
        print("Hmm... I don't understand this input. Try again!")
        
    
    print( 'Game over!' )
    print(f"The number was {randomNumber}")
    print( '###############' )
    print( 'Restarting game' )
