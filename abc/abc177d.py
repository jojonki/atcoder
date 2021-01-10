M = int(1e9) + 7


def main():
    S = int(input())
    # print(S)
    dp = [0] * (S + 1)
    dp[0] = 1
    for v in range(1, S + 1):
        for d in range(v - 3 + 1):
            dp[v] += dp[d]
    # print(dp)
    print(dp[S] % M)


def main_fast():
    S = int(input())
    # print(S)
    dp = [0] * (S + 1)
    dp[0] = 1
    for v in range(3, S + 1):
        dp[v] = (dp[v - 1] + dp[v - 3]) % M
    print(dp[S] % M)


# main()
main_fast()
