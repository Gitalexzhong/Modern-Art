import importlib
import sys
import time
from utility import grid_mask_print, import_map_2d

map_name = sys.argv[1]
algo_name = sys.argv[2]
output_name = sys.argv[3]

def paint():
    size_v, size_h, quota, arr = import_map_2d(map_name)
    
    algo = importlib.import_module("algorithm." + algo_name)
    mask, score = algo.solve(size_v, size_h, arr, quota)

    grid_mask_print(arr, size_v, size_h, mask, score, output_name, quota)

if __name__ == "__main__":
    start_time = time.time()
    paint()
    print("Seconds: " + str(time.time() - start_time))