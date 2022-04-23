


def paint(fname):
    f = open(f"Maps/{fname}", "r")
    l, b, quota = f.readline().split(' ')

    arr = [[char for char in line] for line in f.read().splitlines()]

    print(arr)


if __name__ == "__main__":
    paint("sample10_1")