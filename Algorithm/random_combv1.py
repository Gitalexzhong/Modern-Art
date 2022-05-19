# Combinatorics based random solver 
# Complete non optimal solver, runs for 10000 combinations 

import math
from utility import random_combination, wrapped_tester

def solve(l, b, arr, quota):
    print("Algo: Rand Comb 1.0")

    cords = [(aq, ab) for aq in range(l) for ab in range(b)]

    max_score = 0
    output_map = ()
    weighted_score = -1
    
    for iterC in range(100000):
        test = random_combination(cords, quota)

        if wrapped_tester(list(test)):
            score = 0 

            for i, j in test:
                score += int(arr[i][j])

            weighted_score = round(min(1, math.exp(0.0015*(score-7500)))*100,10)
            
            if weighted_score > max_score:
                max_score = weighted_score
                output_map = test
        
    return output_map, weighted_score
