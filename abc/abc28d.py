import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from itertools import product


def main():
    N, K = read_ints()
    ct = 0

    # K, K, K
    ct += 1

    # K, K, *
    ct += 3 * (N - 1)

    # K, *, *
    ct += 3 * (K - 1) * (N - K) * 2

    print(ct / (N**3))


main()
