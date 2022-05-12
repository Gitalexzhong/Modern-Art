import importlib
import sys
import time
from utility import grid_mask_print, import_map_2d

map_name = sys.argv[1]
algo_name = sys.argv[2]
output_name = sys.argv[3]

def paint():
    l, b, quota, arr = import_map_2d(map_name)

    algo = importlib.import_module("algorithm." + algo_name)
    mask, score = algo.solve(l, b, arr, quota)

    grid_mask_print(arr, l, b, mask, score, output_name)

paint()