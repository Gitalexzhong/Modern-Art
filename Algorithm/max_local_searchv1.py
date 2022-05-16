# Local search based on select a max value first

import math
import random
from re import M
from utility import random_combination, wrapped_tester

def solve(height, length, arr, quota):
    
    max_value = max([max(val) for val in arr])
    listCordsMax = [];

    returnListCords = []

    visitedMap = {}
    pq = {}
    score = 0

    # get max values list 
    for i in range(height):
        for j in range(length):
            if arr[i][j] == max_value:
                listCordsMax.append((i, j))

    chosenStart = random.choice(listCordsMax)
    returnListCords.append(chosenStart)
    visitedMap[chosenStart] = True

    # testCord = 
    # print(random.choice(listCordsMax))
    # print(returnListCords)

    # print(visitedMap)
    # print(testCord[0], testCord[1])
    x, y = chosenStart
    for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
    #     # if direction in cords:
    #         # queue.append(direction)
    #         # cords.remove(direction)
        # print(a,b)
        # if a in range(0, l) and b in range(0, b) and ((6, 2)) not in visitedMap:       
        if a in range(0, height) and b in range(0, length) and (a, b) not in visitedMap:

            # print(a,b, arr[a][b])
            if arr[a][b] in pq:
                pq[arr[a][b]].append((a, b))
            else: 
                pq[arr[a][b]] = [(a,b)]
        
    # print(pq)
    # print()

    for _ in range(quota - 1):
        maxKey = max(pq.keys())

        # print(maxKey)
        # print(pq)

        newSelected = random.choice(pq[maxKey])
        visitedMap[newSelected] = True
        pq[maxKey].remove(newSelected)
        if pq[maxKey] == []:
            del pq[maxKey]

        score += int(maxKey)

        x, y = newSelected
        for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:      
            if a in range(0, height) and b in range(0, length) and (a, b) not in visitedMap:

                if arr[a][b] in pq:
                    pq[arr[a][b]].append((a, b))
                else: 
                    pq[arr[a][b]] = [(a,b)]

    return visitedMap, score
