# File to access csv file and record results

import time

def record_result(map_name, algo_name, output_name, total_time, score, weighted_score, Num_data):

    f = open("Results/data-results.csv", "a")

    f.write(f"\n{time.ctime()},{map_name},{algo_name},{output_name},{total_time},{score},{weighted_score},{Num_data};")

    f.close()

if __name__ == "__main__":
    record_result()