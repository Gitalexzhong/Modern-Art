# Utility function for the painter function  
# from termcolor import Color

# Function to check if each selection of cord are connected to another selection cord
def wrapped_tester(cords):
    for x, y in cords:
        if len(set([(x-1, y), (x+1, y), (x, y-1), (x, y+1)]) & set(cords)) == 0:
            return False
    
    return True

# Inputs a filename and return a array of values, the length, breadth and size of map to make
def import_map_2d(filename):
    f = open(f"Maps/{filename}", "r")
    l, b, quota = f.readline().split(' ')

    arr = [[char for char in line] for line in f.read().splitlines()]

    return l, b, quota, arr

# Takes in a masked cords and outputs to stdout the masked area
def grid_mask_print(arr, l, b, mask, export_type):
    if export_type == None or export_type == "BNW": 
        for i in range(l):
            for j in range(b):
                if (i, j) in mask:
                    print('#', end='')
                else: 
                    print('.', end='')

            print('')

    return

# Print result based on a coloured grid
def grid_coloured_print(arr, l, b, mask, export_type):
    if export_type == None or export_type == "BNW": 
        for i in range(l):
            for j in range(b):
                if (i, j) in mask:
                    # print('\033[31m' +  + '\033[30m')
                    print('\033[0;31;40m' + arr[i][j] + '\033[0;37;40m', end='')
                    # print(f"\033[1;31;40m{arr[i][j]}\n", end='')
                else: 
                    print(arr[i][j], end='')

            print('')

    return
