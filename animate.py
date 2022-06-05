# shows the process of the solver in an animated way 
OKBLUE = '\033[94m'

def animate_print(length, height, arr, red_mask = [], orange_mask = [], green_mask = [], blue_mask = []):
    printing = ""

    for i in range(length):
        for j in range(height):

            if (i, j) in red_mask:    
                printing += "\033[94m" + arr[i][j] + '\x1b[0m'
            else: 
                printing += arr[i][j]

        printing += '\n'

    print(printing, end="\r")