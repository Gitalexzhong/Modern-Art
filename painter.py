


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

    # alg.brutev1.solve(arr, quota)
    # algorithm.brutev1.solve(arr, quota)
    # solve(arr, quota)
    # brutev1()

    print("hiii")

    importlib.import_module("algorithm." + solve_method)

    # import algorithm.brutev1 
    # import algorithm.{solve_method}

    
    

if __name__ == "__main__":
    start = time.time()
    paint("sample10_1", "brutev1")
    print(f"Seconds: {time.time() - start}")
    # algorithm.brutev1.solve("arr", "quota")
    # algo.brutev1.solve("arr", "quota")

