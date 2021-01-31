import math
import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


eps = 1e-7


def get_factors(N, sort=True):
    # 12 -> 1, 2, 3, 4, 6, 12
    res = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i != 0:
            continue
        res.append(i)  # 12 / 2 = 6
        res.append(N // i)  # 12 / 6 = 2

    if sort:
        res.sort()

    return res


def main():
    N = int(input())
    ans = 0
    for L in get_factors(2 * N):
        if (2 * N // L - L + 1) % 2 == 0:
            ans += 1
    print(ans)


main()
