import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main_oroka():
    A, B, C = read_ints()
    for k in range(100000000):
        if (C + B * k) % A == 0:
            print('YES')
            return
    print('NO')


def main():
    A, B, C = read_ints()
    for k in range(B + 1):
        if (A * k) % B == C:
            print('YES')
            return
    print('NO')


main()
