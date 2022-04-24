


import itertools
import math


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
        s = 0 
        for i, j in test:
            s += int(arr[i][j])

        sa = round(min(1, math.exp(0.0015*(s-7500)))*100,10)
        
        if sa > m:
            m = sa
            ma = s
    
    print(m, ma)


if __name__ == "__main__":
    paint("sample10_1")