# Local search based on select a max value first
# Compared to V1, searches will be based on a nearby utility value

import random

def solve(height, length, arr, quota):
    print("Algo: Max Local Search 3.0")
    max_value = max([max(val) for val in arr])
    bestScore = 0
    bestMap = None

    # get max values list 
    for i in range(height):
        for j in range(length):
            if arr[i][j] == max_value:
                visitedMap, score = solve_local_based(height, length, arr, quota, (i, j))
                if score > bestScore:
                    bestMap, bestScore = visitedMap, score

    return bestMap, bestScore

def solve_local_based(height, length, arr, quota, chosenStart):
    visitedMap, pq = {}, {}
    visitedMap[chosenStart] = 1
    score = int(arr[chosenStart[0]][chosenStart[1]])

    pq = check_visited(height, length, chosenStart, pq, visitedMap, arr)

    for i in range(quota - 1):
        
        maxKey = max(pq.keys())
        newSelected = random.choice(pq[maxKey])
        
        visitedMap[newSelected] = i + 2
        pq[maxKey].remove(newSelected)
        if pq[maxKey] == []:
            del pq[maxKey]

        score += int(maxKey)

        pq = check_visited(height, length, newSelected, pq, visitedMap, arr)

    return visitedMap, score

def check_visited(height, length, chosen, pq, visitedMap, arr):
    x, y = chosen
    for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:     
        if a in range(0, height) and b in range(0, length) and (a, b) not in visitedMap and (arr[a][b] not in pq or (a, b) not in pq[arr[a][b]]):
            if arr[a][b] in pq:
                pq[arr[a][b]].append((a, b))
            else: 
                pq[arr[a][b]] = [(a, b)]
    
    return pq
