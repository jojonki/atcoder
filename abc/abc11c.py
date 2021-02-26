import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    NG = set()
    NG.add(int(input()))
    NG.add(int(input()))
    NG.add(int(input()))
    ct = 0
    while N > 0:
        if N in NG:
            print('NO')
            return

        if ct >= 100:
            print('NO')
            return

        if N <= 3:
            print('YES')
            return

        if N - 3 not in NG:
            N -= 3
        elif N - 2 not in NG:
            N -= 2
        elif N - 1 not in NG:
            N -= 1
        else:
            print('NO')
            return
        ct += 1


main()
