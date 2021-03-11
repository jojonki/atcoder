import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, K = read_ints()
    R = read_int_list()
    R.sort()

    C = 0
    for r in R[N - K:]:
        C = (C + r) / 2
    print(C)


main()
