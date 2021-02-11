import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import ceil

from itertools import permutations


def main():
    N, M, L = read_ints()
    P, Q, R = read_ints()
    ans = 0
    for p, q, r in permutations([P, Q, R]):
        ans = max(ans, (N // p) * (M // q) * (L // r))
    print(ans)


main()
