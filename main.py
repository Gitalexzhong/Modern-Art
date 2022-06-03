import importlib
import sys
import time
from output import output_result
from results import record_result
from utility import import_map_2d

map_name = sys.argv[1]
algo_name = sys.argv[2]
output_name = sys.argv[3]

def main():
    start_time = time.time()

    length, height, quota, arr = import_map_2d(map_name)
    
    algo = importlib.import_module("algorithm." + algo_name)
    mask, score = algo.solve(length, height, arr, quota)

    weighted_score = output_result(arr, length, height, mask, score, output_name, quota)

    total_time = time.time() - start_time
    print("Seconds: " + str(total_time))

    record_result(map_name, algo_name, output_name, total_time, score, weighted_score, length*height)

if __name__ == "__main__":
    main()
    