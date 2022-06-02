# File to access csv file and record results

def record_result():
    print("hi")

    f = open("Maps/sample5_1", "r")

    print(f.read())

if __name__ == "__main__":
    record_result()