# FIle for output code and graphs 

from utility import get_weighed_max_score
from colorama import Fore, Style

# Takes in a masked cords and outputs to stdout the masked area
def output_result(arr, length, height, mask, score, export_type, quota):
    print_algo = export_type.lower()

    if print_algo == "grid_coloured_print": 
        grid_coloured_print(length, height, arr, mask)
    else: 
        basic_print(length, height, mask)

    print_scores(score, arr, quota)

    return

def print_scores(score, arr, quota):
    print(f"Score: {score}")
    print(f"Weighted Score: {get_weighed_max_score(score, arr, quota)}%")

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
    for i in range(length):
        for j in range(height):

            if (i, j) in mask:
                print(Fore.RED + str(arr[i][j]) + Style.RESET_ALL, end='')
            else: 
                print(arr[i][j], end='')

        print('')
