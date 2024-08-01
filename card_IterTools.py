"""The itertools module in Python provides a set of fast, memory-efficient tools for performing iterator algebra. These tools are intended to be fast and use as little memory as possible, which makes them useful for handling large data sets. The module contains functions for creating iterators for efficient looping, creating combinatorial iterators, and generating infinite sequences.


import itertools
for i in itertools.count(10, 2): it is (start and step )so the step is 2 as numner will be printed by stepping by number 2 
    print(i)
    if i > 20:
        break
        
        output is 
10
12
14
16
18
20
22
as the i>20 but the 22 prints because print ststement is first so it first prints and then checks

import itertools
count = 0
for item in itertools.cycle('AB'):
    print(item)
    count += 1
    if count > 5:
        break
        
        >a b a b a b
        
        
        
for item in itertools.repeat('A', 3):
    print(item)
> A
  A
  A
  
  
  
itertools.chain
import itertools
import itertools
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list(itertools.chain(list1, list2)))

>[1, 2, 3, 4, 5, 6]


import itertools
data = [1, 2, 3, 4, 5, 6]
print(list(itertools.filterfalse(lambda x: x % 2 == 0, data)))

>[1,3,5]

#*and the needy one 
#*itertools.product
This means it returns all possible combinations of the input iterables where the order of the items matters. It's useful for generating combinations of items, especially when dealing with multiple dimensions.\
#*itertools.product is a powerful function for generating Cartesian products, making it a versatile too


import itertools

list1 = [1, 2]
list2 = ['a', 'b']
result = itertools.product(list1, list2)

for item in result:
    print(item)
    
(1, 'a')
(1, 'b')
(2, 'a')
(2, 'b')

"""
import itertools
import random

# Step 1: Create the deck of cards
list1 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
list2 = ["spade", "club", "heart", "diamond"]
deck = list(itertools.product(list1, list2))

# Step 2: Shuffle the deck
random.shuffle(deck)

# Step 3: Distribute the cards to players
def distribute_cards(deck, num_players):
    num_cards_per_player = 4
    players = [[] for _ in range(num_players)]
    """
The line players = [[] for _ in range(num_players)] creates a list of empty lists, where each empty list corresponds to a player. This setup allows us to store the cards dealt to each player.
    """
    
    for i in range(num_cards_per_player):
        for player in players:
            if deck:
                player.append(deck.pop())
    
    return players

# Ask the user for the number of players (2 to 4)
while True:
    try:
        num_players = int(input("Enter the number of players (2 to 4): "))
        if 2 <= num_players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 2 and 4.")

# Distribute the cards
players = distribute_cards(deck, num_players)

# Print the cards for each player
for i, player in enumerate(players):
    print(f"Player {i + 1}'s cards: {player}")
    
    """Enumerate Players:

enumerate(players) returns both the index and the value (player's card list) from the players list.
i is the index of the current player in the players list (starting from 0).
player is the list of cards for the current player.
Print Player's Cards:

print(f"Player {i + 1}'s cards: {player}") is an f-string used to format the output.
f"Player {i + 1}'s cards: {player}" creates a string where {i + 1} is replaced with the player's number (1-based index) and {player} is replaced with the list of cards for that player.
i + 1 is used because player indices in enumerate(players) start from 0, but we want to display player numbers starting from 1.
"""



