"""
This is a combination problem. Originally did not know there was an external library and kept trying to make all combinations, however wasn't very efficient
Therefore found itertools combnations, this took two parameters, the first was easy, but to find out how many per combo was difficult.
It was more trial and error then found num_buns - num_required + 1 worked.
Then for each combo it adds them up sequentially to the location of each combo
"""

#imports required function
from itertools import combinations

def solution(num, required):
    # Generates an empty 2D list
    keys = [[] for x in xrange(num)]
    
    # Found that test 5 gives invalid parameters to the problem, so returns empty list
    if num < required:
        return keys
    
    #Calculate all possible combos
    numPerBun = (num - required) + 1
    combos = combinations(xrange(num), numPerBun)
    
    #Add the combinations to each bunny
    for combo in enumerate(combos):
        for counter in combo[1]:
            keys[counter] += [combo[0]]
    
    return keys