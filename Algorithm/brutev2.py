# Combinatorics based brute force solver with limitions of up to 3 mins  
# This is due to a time limitation and loops not working with shorter computes 
# Has basic non valid grid checker

import itertools
import math
from utility import wrapped_tester
import time

def solve(l, b, arr, quota):
    print("Algo: Brute 2.0")

    cords = [(aq, ab) for aq in range(l) for ab in range(b)]

    max_score = 0
    timestart = time.time()
    
    for test in itertools.combinations(cords, quota):

        if (time.time() - timestart) > 180:
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
