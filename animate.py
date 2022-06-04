# shows the process of the solver in an animated way 

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
