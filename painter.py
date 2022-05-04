import importlib
import time
from utility import grid_mask_print, import_map_2d

def paint(fname, solve_method = None, export_type = None):
    l, b, quota, arr = import_map_2d(fname)

    algo = importlib.import_module("algorithm." + solve_method)
    mask, score = algo.solve(l, b, arr, quota)

    grid_mask_print(arr, l, b, mask, score, export_type)

if __name__ == "__main__":
    
    start = time.time()
    paint("sample10_1", "brutev1", "grid_coloured_print")
    print(f"Seconds: {time.time() - start}")
