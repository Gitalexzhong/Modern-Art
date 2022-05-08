# Combinatorics based random solver 
# Complete non optimal solver, runs for 10000 combinations 

import importlib
import itertools
import math
import random
from utility import wrapped_tester
from math import comb

def solve(l, b, arr, quota):
    print("Algo: Rand Comb 1.0")

    cords = [(aq, ab) for aq in range(l) for ab in range(b)]

    max_score = 0
    
    # print(random_combination(cords, quota))
    for i in range(1000):
        test = random_combination(cords, quota)
        print(i)

        if wrapped_tester(test):
            score = 0 

            for i, j in test:
                score += int(arr[i][j])

            weighted_score = round(min(1, math.exp(0.0015*(score-7500)))*100,10)
            
            if weighted_score > max_score:
                max_score = weighted_score
                output_map = test
        
    return output_map, weighted_score
    return ((1,1), (1,2), (1,3), (1,4)), 5

def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)
