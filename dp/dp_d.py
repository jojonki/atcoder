def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


# def main():
#     N, W = read_ints()
#     dp = [[0] * (W + 1) for _ in range(N + 1)]
#     w, v = [], []
#     for _ in range(N):
#         _w, _v = read_ints()
#         w.append(_w)
#         v.append(_v)

#     for i in range(N):
#         w_i = w[i]
#         v_i = v[i]
#         # i個目まで選んだときの，重さsum_wまでの最大価値
#         for sum_w in range(W + 1):
#             res = dp[i + 1][sum_w]
#             # 品物iを選んで価値v[i]を獲得
#             if sum_w >= w_i:
#                 res = max(res, dp[i][sum_w - w_i] + v_i)

#             # 品物iはパスして価値は変わらず
#             res = max(res, dp[i][sum_w])

#             dp[i + 1][sum_w] = res

#     print(dp[N][W])


def main():
    N, W = read_ints()
    Items = []
    for _ in range(N):
        w, v = read_ints()
        Items.append((w, v))

    # dp[i][w]: アイテムi個目まで考えて重さwまでの最大価値
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        w_i, v_i = Items[i - 1]
        for sum_w in range(W + 1):
            tmp_v = dp[i - 1][sum_w]
            if sum_w >= w_i:
                tmp_v = max(tmp_v, dp[i - 1][sum_w - w_i] + v_i)
            dp[i][sum_w] = tmp_v
    print(dp[N][W])


main()
