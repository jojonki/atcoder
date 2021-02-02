import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    n = int(input())
    a = read_int_list()
    ans = 0
    for i in range(1, n):
        ans += a[i] - a[i - 1]
    print(ans / (n - 1))


main()
