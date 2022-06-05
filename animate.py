# shows the process of the solver in an animated way 

def animate(length, height, arr, red_mask = [], orange_mask = [], green_mask = [], blue_mask = []):
    printing = ""

    for i in range(length):
        for j in range(height):

            if (i, j) in red_mask:    
                printing += "\x1b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m" + arr[i][j] + '\x1b[0m'
            else: 
                printing += arr[i][j]

        print('')
