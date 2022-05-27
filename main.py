import importlib
import sys
import time
from output import output_result
from utility import import_map_2d

map_name = sys.argv[1]
algo_name = sys.argv[2]
output_name = sys.argv[3]

def main():
    length , height, quota, arr = import_map_2d(map_name)
    
    algo = importlib.import_module("algorithm." + algo_name)
    mask, score = algo.solve(length, height, arr, quota)

    output_result(arr, length, height, mask, score, output_name, quota)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Seconds: " + str(time.time() - start_time))
    