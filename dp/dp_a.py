import sys
sys.setrecursionlimit(20000000)

INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main_morau():
    N = int(input())
    H = read_int_list()
    dp = [float('inf')] * N
    dp[0] = 0
    dp[1] = abs(H[1] - H[0])
    for i in range(2, N):
        dp[i] = min(
            abs(H[i] - H[i - 1]) + dp[i - 1],
            abs(H[i] - H[i - 2]) + dp[i - 2])
    print(dp[N - 1])


def main_kubaru():
    N = int(input())
    H = read_int_list()
    dp = [float('inf')] * N
    dp[0] = 0
    for i in range(N - 1):
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i + 1] - H[i]))
        if i < N - 2:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i + 2] - H[i]))
    print(dp[N - 1])


def rec(dp, H, i):
    if dp[i] < INF:
        return dp[i]

    if i == 0:
        return 0

    res = INF
    # from i-i
    res = min(res, rec(dp, H, i - 1) + abs(H[i] - H[i - 1]))
    # from i-2
    if i >= 2:
        res = min(res, rec(dp, H, i - 2) + abs(H[i] - H[i - 2]))
    # print('dp', i, '=', res)
    dp[i] = res
    return res


def main_memo_rec():
    N = int(input())
    H = read_int_list()
    dp = [float('inf')] * N
    print(rec(dp, H, N - 1))


# main_kubaru()
# main_morau()
main_memo_rec()
