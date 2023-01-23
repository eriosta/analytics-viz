import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math
import sys, os

# Roll die
def rollDie( m ):
    """
    This function creates a random number between 1 and m inclusive and returns it.

    Parameters
    ----------
    m : int
        Upper bound of random number

    Returns
    -------
    int
        A random number between 1 and m inclusive
    """
    die = random.randrange( 1, m + 1 ) 
    return die

# Get key
def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore print
def enablePrint():
    sys.stdout = sys.__stdout__

# Simulate games
def simulateGames(n,verbose=False):

    """
    This function simulateGame simulates several rounds of the game. See the rules above for how each game
    round is played.
    
    Parameters
    ----------
    n : int
        The number of games

    verbose : bool
        Show all print statements throughout the game except the final print statement with the score board after n games. Default is False.
        
    Returns
    -------
    wins : dictionary
        A dictionary with keys 'player', 'banker', 'tie'. All the values should be zero.
    """

    if verbose==True:
        enablePrint()
    else:
        blockPrint()

    wins = {'PLAYER':0, "BANKER":0, "TIE":0}

    for round in np.arange(1,n+1):

        rolls = {'PLAYER':rollDie(6), "BANKER":rollDie(6)}

        print(f"Round {round}")

        print(f"PLAYER rolled a %s and BANKER rolled a %s" % (rolls["PLAYER"],rolls["BANKER"]))

        # If roll 6
        if rolls["PLAYER"] == 6 or rolls["BANKER"] == 6:
            print(" ")
            print(f"Game stoped because {get_key(6,rolls)} rolled a 6")
            if wins["BANKER"] > wins["PLAYER"]:
                print("BANKER wins with", wins["BANKER"])
            elif wins["PLAYER"] > wins["BANKER"]:
                print("PLAYER wins with", wins["PLAYER"])
            else:
                print("No winner. It's a tie!")
            print("###################")
            pass
        # If tie
        elif rolls["PLAYER"] == rolls["BANKER"]:
            print("There is a tie!")
            wins["TIE"] = wins["TIE"] + 1

        elif rolls["BANKER"] <= 3:
            rolls["BANKER"] = rollDie(6)
        
        elif rolls["PLAYER"] <= 2:
            rolls["PLAYER"] = rollDie(6)

        if rolls["BANKER"] > rolls["PLAYER"]:
            wins.update({"BANKER": wins["BANKER"] + 1})

        elif rolls["PLAYER"] > rolls["BANKER"]:
            wins.update({"PLAYER":wins["PLAYER"]+1})

        print("###################")
        print("PLAYER:",wins["PLAYER"])
        print("BANKER:",wins["BANKER"])
        print("###################")
        print("")
        print("")

    enablePrint()
    if wins["BANKER"] > wins["PLAYER"]:
        print("BANKER wins with", wins["BANKER"])
    elif wins["PLAYER"] > wins["BANKER"]:
        print("PLAYER wins with", wins["PLAYER"])
    else:
        print("No winner. It's a tie!")
    
    return wins
    
def visualizeResults(n):
    """
    This function creates a bar plot of frequencies for each outcome using the seaborn package. 
    It will show the frequency of outcomes for the PLAYER, BANKER, and TIE out of 100%. Recall
    that wins dictionary parameter has a total count of outcomes and that you will need
    to find the percentage of occurrences. 
    
    Parameters
    ----------
    n : int
        The number of games
        
    Returns
    -------
    None
    """
    wins = simulateGames(n)
    players = list(wins.keys())
    scores = [wins[k] for k in players]
    sns.barplot(x=players, y=scores)
    plt.show()

# Visualize games
visualizeResults(n=200000)