import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    vals = read_int_list()
    vals.sort()
    A, B, C = vals[0], vals[1], vals[2]
    if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
        print(0)
    else:
        print(A * B)


main()
