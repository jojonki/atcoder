import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    m, n = read_ints()
    m = m % 12
    d_m = 360.0 * (m / 12) + 30 * (n / 60)
    d_n = 360 * (n / 60)

    d = abs(d_m - d_n)
    d = min(d, 360.0 - d)
    print(d)


main()
