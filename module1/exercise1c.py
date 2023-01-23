import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math
import sys, os

# Roll die
def rollDie( m ):
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
    wins = simulateGames(n)
    players = list(wins.keys())
    scores = [wins[k] for k in players]
    sns.barplot(x=players, y=scores)
    plt.show()

# Visualize games
visualizeResults(n=200000)