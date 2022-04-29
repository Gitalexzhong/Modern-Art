import importlib
import time
from utility import import_map 

def paint(fname, solve_method = None):
    l, b, quota, arr = import_map(fname)

    a = importlib.import_module("algorithm." + solve_method)

    a.solve(arr, quota)

if __name__ == "__main__":
    start = time.time()
    paint("sample10_1", "brutev1")
    print(f"Seconds: {time.time() - start}")

