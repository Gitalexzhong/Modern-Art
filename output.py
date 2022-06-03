# FIle for output code and graphs 

from utility import get_min_max, get_weighed_max_score
from colorama import Fore, Style
from termcolor import colored

# Takes in a masked cords and outputs to stdout the masked area
def output_result(arr, length, height, mask, score, export_type, quota):
    print_algo = export_type.lower()

    if print_algo == "grid_coloured_print": 
        grid_coloured_print(length, height, arr, mask)

    elif print_algo == "grid_heat_print": 
        grid_heat_print(length, height, arr, mask)

    else: 
        basic_print(length, height, mask)

    return print_scores(score, arr, quota)

def print_scores(score, arr, quota):
    weighted_score = get_weighed_max_score(score, arr, quota)
    print(f"Score: {score}")
    print(f"Weighted Score: {weighted_score}%")

    return weighted_score

def basic_print(length, height, mask):
    for i in range(length):
        for j in range(height):

            if (i, j) in mask:
                print('#', end='')
            else: 
                print('.', end='')

        print('')

def grid_coloured_print(length, height, arr, mask):
    for i in range(length):
        for j in range(height):

            if (i, j) in mask:
                print(Fore.RED + str(arr[i][j]) + Style.RESET_ALL, end='')
            else: 
                print(arr[i][j], end='')

        print('')

def grid_heat_print(length, height, arr, mask):
    minV, maxV = get_min_max(arr)
    diff = maxV - minV

    for i in range(length):
        for j in range(height):

            r,g,b = rgb(minV, maxV, int(arr[i][j]))
            if (i, j) in mask:    
                print("\x1b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m" + arr[i][j] + '\x1b[0m', end='')
            else: 
                print(arr[i][j], end='')

        print('')

def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))
    r = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r

    return r, g, b
