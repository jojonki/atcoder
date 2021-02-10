import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import sqrt


def main():
    x1, y1, x2, y2, T, V = read_ints()
    N = int(input())
    for _ in range(N):
        x, y = read_ints()
        d2 = sqrt((x - x1)**2 + (y - y1)**2) + sqrt((x2 - x)**2 + (y2 - y)**2)
        if d2 / V <= T:
            print('YES')
            return
    print('NO')


main()
