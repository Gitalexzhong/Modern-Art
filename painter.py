


import importlib
import itertools
import math
import time 
# import Algorithm as algo
# from algorithm import *

def paint(fname, solve_method = None):
    f = open(f"Maps/{fname}", "r")
    l, b, quota = f.readline().split(' ')

    arr = [[char for char in line] for line in f.read().splitlines()]

    print("hiii")

    a = importlib.import_module("algorithm." + solve_method)

    a.solve(arr, quota)
    

if __name__ == "__main__":
    start = time.time()
    paint("sample10_1", "brutev1")
    print(f"Seconds: {time.time() - start}")

