import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from itertools import combinations


def main():
    N = int(input())
    P = read_int_list()
    dp = [[0] * 10010 for _ in range(N + 1)]
    unique = {0}
    for i in range(1, N + 1):
        p = P[i - 1]
        for sum_p in range(10010):
            tmp_p = dp[i - 1][sum_p]
            if sum_p >= p:
                tmp_p = max(tmp_p, dp[i - 1][sum_p - p] + p)
            dp[i][sum_p] = tmp_p
            unique.add(tmp_p)
    print(len(unique))


main()
