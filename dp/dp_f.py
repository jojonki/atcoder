def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    s, t = input(), input()
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    # dp[0][0] = 0
    for i in range(len(s)):
        for j in range(len(t)):
            res = dp[i + 1][j + 1]
            if s[i] == t[j]:
                res = max(res, dp[i][j] + 1)
            res = max(res, dp[i + 1][j])
            res = max(res, dp[i][j + 1])
            dp[i + 1][j + 1] = res

    # print(dp[len(s)][len(t)])
    # for i in range(len(s)):
    #     print(dp[i])

    # reconstruction
    ans = ''
    i, j = len(s), len(t)
    while i > 0 and j > 0:
        while i > 0 and dp[i][j] == dp[i - 1][j]:
            i -= 1
        while j > 0 and dp[i][j] == dp[i][j - 1]:
            j -= 1
        if i > 0:
            ans += s[i - 1]
        i -= 1
        j -= 1
    print(ans[::-1])


main()
