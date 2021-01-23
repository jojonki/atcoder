def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


import math


def main():
    a, b = input().split()
    v = int(a + b)

    # print(math.sqrt(v), int(math.sqrt(v)))
    if math.sqrt(v) == int(math.sqrt(v)):
        print('Yes')
    else:
        print('No')


main()
