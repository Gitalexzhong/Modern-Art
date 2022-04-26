


import itertools
import math
import time 
# import Algorithm as algo
import algorithm.brutev1


def paint(fname, solve_method = None):
    f = open(f"Maps/{fname}", "r")
    l, b, quota = f.readline().split(' ')

    arr = [[char for char in line] for line in f.read().splitlines()]

    print(arr)

    print(solve_method)

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
                ma = s
    
    print(m, ma)

    # alg.brutev1.solve(arr, quota)

    

def wrapped_tester(cords):
    for x, y in cords:
        if len(set([(x-1, y), (x+1, y), (x, y-1), (x, y+1)]) & set(cords)) == 0:
            return False
    
    return True


if __name__ == "__main__":
    # start = time.time()
    # paint("sample10_1")
    # print(f"Seconds: {time.time() - start}")
    algorithm.brutev1.solve("arr", "quota")
    # algo.brutev1.solve("arr", "quota")

