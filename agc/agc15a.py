import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, A, B = read_ints()
    if A > B:
        print(0)
        return

    if A == B or N == 2:
        print(1)
        return

    if N - 2 < 0:
        print(0)
        return

    print((B - A) * (N - 2) + 1)


main()
