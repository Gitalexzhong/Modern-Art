# Python program used in creating and testing programs or maps

import random

from utility import import_map_2d

def generate_grid(size, quota):
    print(size, size, quota)
    for i in range(size):
        for j in range(size):
            print(random.randint(0,9), end='')
        print()

def get_distribution(arr): 
    l = {}

    for i in arr: 
        for j in arr: 
            if j in l: 
                l[j] += 1
            else:
                l[j] = 1

    return l


if __name__ == '__main__':
    # print(wrapped_tester([(1,1),(1,2),(1,4),(1,5)]))
    # generate_grid(10, 15)
    size_v, size_h, quota, arr = import_map_2d("sample1000_1")
    print(get_distribution())