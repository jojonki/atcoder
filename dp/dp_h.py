def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


D = int(10**9 + 7)


def main():
    H, W = read_ints()
    table = []
    for _ in range(H):
        table.append(list(input()))
    # print(table)
    dp = [[0] * W for _ in range(H)]
    # dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                dp[0][0] = 1
                continue
            if table[i][j] == '#':
                continue
            from_left, from_top = 0, 0
            if j > 0 and table[i][j - 1] != '#':
                from_left = dp[i][j - 1]
            if i > 0 and table[i - 1][j] != '#':
                from_top = dp[i - 1][j]
            # print(i, j, from_left, from_top)
            dp[i][j] = (from_left % D + from_top % D) % D
    print(dp[H - 1][W - 1])


main()
