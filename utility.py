# Utility function for the painter function  
import random
from colorama import Fore, Style
import math
import numpy as np

# Inputs a filename and return a array of values, the length, breadth and size of map to make
def import_map_2d(filename):
    f = open(f"Maps/{filename}", "r")
    v, h, quota = f.readline().split(' ')

    arr = [[char for char in line] for line in f.read().splitlines()]

    return int(v), int(h), int(quota), arr

# Function to check if each selection of cord are connected to another selection cord, implements a queue system
def wrapped_tester(cords):
    queue = [cords[0]]
    cords.pop(0)
    i = 0

    while i < len(queue): 
        x, y = queue[i]
        for direction in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if direction in cords:
                queue.append(direction)
                cords.remove(direction)
        
        queue.pop(0)

    if len(cords) > 0:
        return False
    else: 
        return True

# Custom code to generate random combinatorics of cords
def random_combination(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)

def get_weighed_max_score(score, arr, quota): 
    flatArr = np.array(arr, int).flatten()
    flatArr.sort()
    totalMaxScore = np.sum(flatArr[-quota:])
    return round(score*100/totalMaxScore, 8)

if __name__ == '__main__':
    print(wrapped_tester([(1,1),(1,2),(1,4),(1,5)]))
    
