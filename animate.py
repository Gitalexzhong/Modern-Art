# shows the process of the solver in an animated way 
import sys
import time

OKBLUE = '\033[94m'

def animate_print(length, height, arr, red_mask = [], yellow_mask = [], green_mask = [], blue_mask = []):
    printing = ""

    for i in range(length):
        for j in range(height):

            if (i, j) in red_mask:    
                printing += "\033[31m" + arr[i][j] + '\x1b[0m'
            elif (i, j) in yellow_mask:    
                printing += "\033[33m" + arr[i][j] + '\x1b[0m'
            elif (i, j) in green_mask:    
                printing += "\033[32m" + arr[i][j] + '\x1b[0m'
            elif (i, j) in blue_mask:    
                printing += "\033[34m" + arr[i][j] + '\x1b[0m'
            else: 
                printing += arr[i][j]

        printing += '\n'

    time.sleep(0.005)
    print(printing, end='\n')