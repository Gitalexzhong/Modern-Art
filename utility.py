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

# Takes in a masked cords and outputs to stdout the masked area
def grid_mask_print(arr, l, b, mask, score, export_type, quota):
    if export_type == None or export_type == "BNW": 

        for i in range(l):
            for j in range(b):

                if (i, j) in mask:
                    print('#', end='')
                else: 
                    print('.', end='')

            print('')

    elif export_type == "grid_coloured_print": 
        
        for i in range(l):
            for j in range(b):

                if (i, j) in mask:
                    print(Fore.RED + str(arr[i][j]) + Style.RESET_ALL, end='')
                else: 
                    print(arr[i][j], end='')

            print('')
        
    weighted_score = round(min(1, math.exp(0.0015*(score-7500)))*10,10)
    print(f"Score: {score}")
    print(f"Weighted Score: {weighted_score}")
    
    print(f"Weighted Score: {get_weighed_max_score(arr, quota)}")
    return

# Custom code to generate random combinatorics of cords
def random_combination(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)
    
def generate_grid(size, quota):
    print(size, size, quota)
    for i in range(size):
        for j in range(size):
            print(random.randint(0,9), end='')
        print()

def get_weighed_max_score(arr, quota): 
    flatArr = np.array(arr).flatten()
    print(np.sort(flatArr))
    flatArr[::-1].sort()
    b = flatArr[:quota]
    v=np.sum(b)
    print(v)
    return 1

if __name__ == '__main__':
    # print(wrapped_tester([(1,1),(1,2),(1,4),(1,5)]))
    generate_grid(10, 15)
