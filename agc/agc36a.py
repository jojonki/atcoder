import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import ceil


def main():
    S = int(input())
    x1, y1 = 0, 0
    x2 = 10**9
    y2 = 1
    y3 = ceil(S / (10**9))
    x3 = (10**9) * y3 - S
    ans = [x1, y1, x2, y2, x3, y3]
    print(*ans)


main()
