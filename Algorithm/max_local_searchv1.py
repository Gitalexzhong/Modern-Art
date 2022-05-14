# Local search based on select a max value first

import math
import random
from utility import random_combination, wrapped_tester

def solve(l, b, arr, quota):
    
    max_value = max([max(x) for x in arr])
    listCordsMax = [];
    returnListCords = []
    visitedMap = []
    pq = {}

    for i in range(l):
        for j in range(b):
            if arr[i][j] == max_value:
                listCordsMax.append((i, j))

    returnListCords.append(random.choice(listCordsMax))
    print(random.choice(listCordsMax))
    print(returnListCords)

    return returnListCords, -1
