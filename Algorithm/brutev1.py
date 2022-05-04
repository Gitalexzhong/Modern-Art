import itertools
import math
from utility import wrapped_tester

def solve(l, b, arr, quota):
    print("Algo: Brute 1.0")

    cords = [(aq, ab) for aq in range(l) for ab in range(b)]

    comb = list(itertools.combinations(cords, quota))

    m = 0
    for test in comb:

        if wrapped_tester(test):
            s = 0 
            for i, j in test:
                s += int(arr[i][j])

            sa = round(min(1, math.exp(0.0015*(s-7500)))*100,10)
            
            if sa > m:
                m = sa
                out = test
            
    return out, sa
