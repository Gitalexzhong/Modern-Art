# Combinatorics based brute force solver with limitions of up to 10k loops 
# This is due to a time limitation 
# Has basic non valid grid checker

import itertools
import math
from utility import wrapped_tester
from math import comb

def solve(l, b, arr, quota):
    print("Algo: Brute 2.0")

    cords = [(aq, ab) for aq in range(l) for ab in range(b)]

    max_score = 0
    no_ops = 1
    
    for test in itertools.combinations(cords, quota):
        no_ops += 1
        print(no_ops)

        if no_ops == 1000000:
            break

        if wrapped_tester(test):
            score = 0 

            for i, j in test:
                score += int(arr[i][j])

            weighted_score = round(min(1, math.exp(0.0015*(score-7500)))*100,10)
            
            if weighted_score > max_score:
                max_score = weighted_score
                output_map = test
        
    return output_map, weighted_score
