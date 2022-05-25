# FIle for output code and graphs 

from utility import get_weighed_max_score
from colorama import Fore, Style
import math

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

    print(f"Score: {score}")
    print(f"Weighted Score: {get_weighed_max_score(score, arr, quota)}%")
    return
