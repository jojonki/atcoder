import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, L = read_ints()
    x = read_int_list()
    T1, T2, T3 = read_ints()
    X = [0] * (L + 1)
    for xx in x:
        X[xx] = T3

    dp = [INF] * (L + 1)
    dp[0] = 0

    for i in range(1, L + 1):
        dp[i] = min(dp[i], dp[i - 1] + T1)
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + T1 + T2)
        if i >= 4:
            dp[i] = min(dp[i], dp[i - 4] + T1 + T2 * 3)

        dp[i] += X[i]

    for j in range(1, 4):
        dp[L] = min(dp[L], dp[L - j] + 0.5 * T1 + (0.5 + j - 1) * T2)

    print(int(dp[L]))


main()
