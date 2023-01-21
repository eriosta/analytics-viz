import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math

# **Rules**

# There are two players: PLAYER and BANKER. These are just names for the players. Each player has a regular six-sided die. 
# In one round, each player will roll their die and attempt to get the highest value. The rules are:

# - If either player rolls a six, the game stops. The player with the higher die value wins. If both dice values are the same, then it is a tie. 
# - If neither player has a six in the initial roll, then a player may re-roll under these conditions:
#     - If the BANKER initially rolled a 3 or below, the BANKER will re-roll their die. 
#     - If the PLAYER initially rolled a 2 or below, the PLAYER will re-roll their die.
#     - After this reroll, the game stops. The player with the higher die value wins. If both dice values are the same, then it is a tie. 

def rollDie( m ):
    die = random.randrange( 1, m + 1 ) 
    return die

def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

def simulateGames( n, wins=None ):
    for round in np.arange(1,n+1):
        print(f"Round {round}")

        rolls = {'PLAYER':rollDie(6), "BANKER":rollDie(6)}

        print(f"PLAYER rolled a %s and BANKER rolled a %s" % (rolls["PLAYER"],rolls["BANKER"]))

        if rolls["PLAYER"] == 6 or rolls["BANKER"] == 6:
            print(f"Game stoped because {get_key(6,rolls)} rolled a 6")
            break

        elif rolls["PLAYER"] == rolls["BANKER"]:
            pass

simulateGames(5)
# Sample driver code
# games = 200000 # Simulate 200000 games
# outcomes = { 'player': 0, 'banker': 0, 'tie': 0 } # Dictionary to keep track of outcomes
# simulateGames( games, outcomes ) # Call function to simulate the games
# visualizeResults( games, outcomes ) # Call function to show bar chart


# >>> books = {}
# >>> books['book'] = 3       
# >>> books['book'] -= 1   
# >>> books   
# {'book': 2}   