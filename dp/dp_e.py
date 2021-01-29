def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


INF = float('inf')


def main():
    N, W = read_ints()
    MAX_V = 100 * 1000 + 10
    dp = [[INF] * (MAX_V) for _ in range(N + 1)]
    dp[0][0] = 0
    w, v = [], []
    for _ in range(N):
        _w, _v = read_ints()
        w.append(_w)
        v.append(_v)

    for i in range(N):
        w_i = w[i]
        v_i = v[i]
        # i個目まで選んだときの，価値sum_vの最小重み
        for sum_v in range(MAX_V):
            res = dp[i + 1][sum_v]
            # 品物iを選んで価値v[i]を獲得
            if sum_v >= v_i:
                res = min(res, dp[i][sum_v - v_i] + w_i)

            # 品物iはパスして重みは変わらず
            res = min(res, dp[i][sum_v])

            dp[i + 1][sum_v] = res

    ans = 0
    for sum_v in range(MAX_V):
        if dp[N][sum_v] <= W:
            ans = max(ans, sum_v)
    print(ans)


main()
