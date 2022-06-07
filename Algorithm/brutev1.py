# Combinatorics based brute force solver 
# Is memory limited and has basic non valid grid checker

import itertools
from utility import wrapped_tester

def solve(l, b, arr, quota):
    print("Algo: Brute 1.0")

    cords = [(aq, ab) for aq in range(l) for ab in range(b)]

    comb = list(itertools.combinations(cords, quota))

    max_score = 0

    for test in comb:
        if wrapped_tester(list(test)):
            score = 0 
            for i, j in test:
                score += int(arr[i][j])
            
            if score > max_score:
                max_score = score
                output_map = test
            
    return list(output_map), max_score
