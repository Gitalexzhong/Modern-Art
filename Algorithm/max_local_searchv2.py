# Local search based on select a max value first
# Compared to V1, searches will be based on a nearby utility value

import math
import random
from re import M
from utility import random_combination, wrapped_tester, grid_mask_print

def solve(height, length, arr, quota):
    
    max_value = max([max(val) for val in arr])
    bestScore = 0
    bestMap = None

    # get max values list 
    for i in range(height):
        for j in range(length):
            if arr[i][j] == max_value:
                return solve_local_based(height, length, arr, quota, (i, j))

                visitedMap, score = solve_local_based(height, length, arr, quota, (i, j))
                if score > bestScore:
                    bestMap, bestScore = visitedMap, score

    return bestMap, bestScore

def solve_local_based(height, length, arr, quota, chosenStart):
    visitedMap, pq = {}, {}
    visitedMap[chosenStart] = 1
    score = 0
    # print(chosenStart)
    # print(visitedMap)
    pq = check_visited(height, length, chosenStart, pq, visitedMap, arr)

    print(pq)
    print(visitedMap)
    grid_mask_print(arr, length, height, visitedMap, -1, "grid_coloured_print", quota)
    print()
    for i in range(quota - 1):
        
        maxKey = max(pq.keys())
        newSelected = random.choice(pq[maxKey])
        
        visitedMap[newSelected] = i + 2
        pq[maxKey].remove(newSelected)
        if pq[maxKey] == []:
            del pq[maxKey]

        score += int(maxKey)
        # print(maxKey)

        pq = check_visited(height, length, newSelected, pq, visitedMap, arr)
        print(pq)
        print(visitedMap)
        grid_mask_print(arr, length, height, visitedMap, -1, "grid_coloured_print", quota)
        print()

    #     print(i)
    # print(visitedMap)
    return visitedMap, score


def check_visited(height, length, chosen, pq, visitedMap, arr):
    x, y = chosen
    print(chosen)
    for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:     
        print("asd: " + str(a) + " " + str(b)) 
        if a in range(0, height) and b in range(0, length) and (a, b) not in visitedMap and (arr[a][b] not in pq or (a, b) not in pq[arr[a][b]]):
            print("input")
            if arr[a][b] in pq:
                pq[arr[a][b]].append((a, b))
            else: 
                pq[arr[a][b]] = [(a, b)]
    
    return pq