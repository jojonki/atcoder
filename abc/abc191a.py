import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    V, T, S, D = read_ints()
    r1, r2 = V * T, V * S
    if r1 <= D <= r2:
        print('No')
    else:
        print('Yes')


main()
