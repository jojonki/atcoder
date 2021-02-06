import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import sqrt


def main():
    ans = INF
    n = int(input())
    for h in range(1, int(sqrt(n)) + 1):
        w = n // h
        amari = n - (w * h)
        ans = min(ans, abs(w - h) + amari)
    print(ans)


main()
