import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from itertools import combinations


def main():
    D = read_int_list()
    P = []
    for a, b, c in combinations(D, 3):
        P.append(a + b + c)
    P.sort()
    print(P[-3])


main()
