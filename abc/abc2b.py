import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import sqrt


def main():
    xa, ya, xb, yb, xc, yc = read_ints()

    a = sqrt((xb - xa)**2 + (yb - ya)**2)
    b = sqrt((xc - xa)**2 + (yc - ya)**2)
    c = sqrt((xc - xb)**2 + (yc - yb)**2)
    s = (a + b + c) / 2
    S = sqrt(s * (s - a) * (s - b) * (s - c))
    print(S)


main()
