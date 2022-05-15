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

    # get max values list 
    for i in range(l):
        for j in range(b):
            if arr[i][j] == max_value:
                listCordsMax.append((i, j))

    chosenStart = random.choice(listCordsMax)
    returnListCords.append(chosenStart)
    visitedMap.append(chosenStart)

    testCord = chosenStart
    # print(random.choice(listCordsMax))
    # print(returnListCords)

    print(visitedMap)
    print(testCord[0], testCord[1])
    x, y = testCord
    for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
    #     # if direction in cords:
    #         # queue.append(direction)
    #         # cords.remove(direction)
        if a in range(0, l) and b in range(0, b):

            print(a, b)


    # pq[(1,1)] = 5
    # print(pq)

    return returnListCords, -1
