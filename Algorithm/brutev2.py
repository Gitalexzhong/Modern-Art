import itertools
import math
from utility import wrapped_tester
from math import comb

def solve(l, b, arr, quota):
    print("Algo: Brute 2.0")

    cords = [(aq, ab) for aq in range(l) for ab in range(b)]

    # comb = list(itertools.combinations(cords, quota))

    m = 0
    no = 1
    noto = comb(l*b,quota)


    # for test in comb:

    #     if wrapped_tester(test):
    #         s = 0 
    #         for i, j in test:
    #             s += int(arr[i][j])

    #         sa = round(min(1, math.exp(0.0015*(s-7500)))*100,10)
            
    #         if sa > m:
    #             m = sa
    #             out = test
    
    
    for test in itertools.combinations(cords, quota):
        print(str(no) + " / " + str(noto))
        no += 1
        print(test)
        if no == 10010:
            break
        if wrapped_tester(test):
            s = 0 
            for i, j in test:
                s += int(arr[i][j])

            sa = round(min(1, math.exp(0.0015*(s-7500)))*100,10)
            
            if sa > m:
                m = sa
                out = test
        
    return out, sa
    # return ((1, 1), (1, 2), (1, 4), (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 4)), 123

