# Utility function for the painter function  

def wrapped_tester(cords):
    for x, y in cords:
        if len(set([(x-1, y), (x+1, y), (x, y-1), (x, y+1)]) & set(cords)) == 0:
            return False
    
    return True

# Function designed to open files based on header for 2d algo
def import_map(filename):
    print("hi")
