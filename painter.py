import importlib
import time
from utility import grid_coloured_print, grid_mask_print, import_map_2d

def paint(fname, solve_method = None, export_type = None):
    l, b, quota, arr = import_map_2d(fname)

    algo = importlib.import_module("algorithm." + solve_method)

    mask = algo.solve(arr, quota)

    grid_coloured_print(arr, int(l), int(b), mask, export_type)

if __name__ == "__main__":
    start = time.time()
    paint("sample10_1", "brutev1")
    print(f"Seconds: {time.time() - start}")

