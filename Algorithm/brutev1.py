import itertools
import math
from utility import wrapped_tester

def solve(arr, quota):
    print("brute")

    # print(arr)

    l = len(arr)
    b = len(arr[0])

    cords = [(aq, ab) for aq in range(int(l)) for ab in range(int(b))]

    comb = list(itertools.combinations(cords, int(quota)))

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
    
    # print(m, ma)
    return out



