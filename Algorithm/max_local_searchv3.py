# Local search based on select a max value first
# Compared to V1, searches will be based on a nearby utility value

from math import sqrt
import math
import operator
import random

incremental_step_value = 1

def solve(height, length, arr, quota):
    print("Algo: Max Local Search 3.0")
    max_value = max([max(val) for val in arr])
    dict_max = {}

    # get max values list 
    for i in range(height):
        for j in range(length):
            if arr[i][j] == max_value:
                dict_max[(i,j)] = 0

    chosen_node = best_node_chooser(arr, dict_max, min(height, length, int(math.sqrt(quota))))
    return solve_local_based(height, length, arr, quota, chosen_node)


def solve_local_based(height, length, arr, quota, chosenStart):
    visitedMap, pq = {}, {}
    visitedMap[chosenStart] = 1
    score = int(arr[chosenStart[0]][chosenStart[1]])

    pq = check_visited(height, length, chosenStart, pq, visitedMap, arr)

    for i in range(quota - 1):
        
        maxKey = max(pq.keys())
        newSelected = best_node_chooser(arr, convert_dict_zero(pq[maxKey]), int(math.sqrt(i)))
        
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

def convert_dict_zero(l):
    d = {}

    for item in l:
        d[item] = 0

    return d
    

def best_node_chooser(arr, node_list, start_val_step = incremental_step_value, step_val = incremental_step_value): 
    max_range = start_val_step

    while (1):
        for x, y in node_list:
            for item_x in range(len(arr)): 
                for item_y in range(len(arr[0])): 
                    distance = sqrt(pow((x - item_x), 2) + pow((y - item_y), 2))
                    if distance <= max_range: 
                        node_list[(x, y)] += int(arr[item_x][item_y])

        max_item_val = max(node_list.values())
        list_max = [key for key in node_list if node_list[key] == max_item_val]
    
        if len(list_max) == 1:
            print(list_max[0], max_item_val)
            return list_max[0]
        print(max_range)
        max_range += step_val

        # TODO add a bypass system for overload 

    return None

if __name__ == '__main__': 
    arr = [['0', '3', '5', '2', '2'], ['0', '9', '4', '6', '8'], ['5', '2', '9', '7', '8'], ['0', '4', '4', '1', '6'], ['2', '3', '8', '0', '7']]
    node_list = {(1, 1): 0, (2, 2): 0}
    best_node_chooser(arr, node_list)