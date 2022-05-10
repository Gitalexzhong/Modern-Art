# Combinatorics based random solver with multicore processing 
# Complete non optimal solver, runs for 10000 combinations 

import importlib
import itertools
import math
import random
from utility import wrapped_tester
from math import comb
import multiprocessing


def solve(l, b, arr, quota):
    print("Algo: Rand Comb 2.0")

    cords = [(aq, ab) for aq in range(l) for ab in range(b)]

    max_score = 0
    output_map = ()
    weighted_score = -1
    
    print(multiprocessing.cpu_count())

    for iterC in range(100000):
        test = random_combination(cords, quota)

        if wrapped_tester(list(test)):
            score = 0 

            print(test)

            for i, j in test:
                score += int(arr[i][j])

            weighted_score = round(min(1, math.exp(0.0015*(score-7500)))*100,10)
            
            if weighted_score > max_score:
                max_score = weighted_score
                output_map = test
        
    return output_map, weighted_score


def random_combination(iterable, r):
    # "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)
