def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


import math


def main():
    a, b = read_ints()
    print(math.ceil((a + b) / 2))


main()
