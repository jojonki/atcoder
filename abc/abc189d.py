def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def f(S):
    N = len(S)
    if N == 0:
        return 1

    if S[-1] == 'AND':
        return f(S[:-1])
    else:  # OR
        return 2**N + f(S[:-1])


def main2():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    ans = f(S)
    print(ans)


def main_snuke():
    N = int(input())
    # dp[0]: Falseになる数
    # dp[1]: Trueになる数
    dp = [1, 1]
    for i in range(N):
        s = input()
        p = [0, 0]
        p, dp = dp, p
        for j in range(2):  # y_i == j
            for x in range(2):  # x
                nj = j
                if s == 'AND':
                    nj &= x
                else:
                    nj |= x
                dp[nj] += p[j]
        print(i, dp)

    print(dp)
    print(dp[1])


def main():
    N = int(input())
    # dp[i][j] = x_iまで決めた，y_i=jになるときの場合の数
    dp = [[0, 0] for _ in range(N + 1)]
    dp[0][0] = 1  # when x_0, y_0=0
    dp[0][1] = 1  # when x_0, y_0=1
    for i in range(N):
        s = input()
        # print(i, dp)
        for j in range(2):  # y_i == j
            if s == 'AND':
                if j == 1:  # y_j == 1
                    dp[i + 1][1] += dp[i][1]
                    dp[i + 1][0] += dp[i][0]
                else:  # y_j == 0
                    dp[i + 1][0] += dp[i][0] + dp[i][1]
            else:  # OR
                if j == 1:  # y_j == 1
                    dp[i + 1][1] += dp[i][0] + dp[i][1]
                else:  # y_j == 0
                    dp[i + 1][1] += dp[i][1]
                    dp[i + 1][0] += dp[i][0]

    print(dp[N][1])
    # print(dp[1])


main()
