import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


H, W = read_ints()
T = []
for _ in range(H):
    T.append(list(input()))
# print(T)
ans = INF


def dfs(r, c, cost):
    global ans
    # print(r, c)
    if cost > ans:
        return
        return INF

    if T[r][c] == '#':
        cost += 1

    if r == H - 1 and c == W - 1:
        ans = min(ans, cost)
        return

    if r == H - 1:
        # print('##1')
        dfs(r, c + 1, cost)
    elif c == W - 1:
        # print('##2')
        dfs(r + 1, c, cost)
    else:
        # print('##3')
        dfs(r, c + 1, cost)
        # print('##4', r, c, r == H - 1)
        dfs(r + 1, c, cost)

    # return cost


def p(dp):
    for i in range(len(dp)):
        print(dp[i])


def main():
    dp = [[INF] * W for _ in range(H)]
    if T[0][0] == '#':
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    for c in range(1, W):
        dp[0][c] = dp[0][c - 1]
        if T[0][c - 1] == '.' and T[0][c] == '#':
            dp[0][c] += 1
        # elif c == W - 1 and T[0][c] == '#':
        #     dp[0][c] += 1

    for r in range(1, H):
        dp[r][0] = dp[r - 1][0]
        if T[r - 1][0] == '.' and T[r][0] == '#':
            dp[r][0] += 1
        # elif r == H - 1 and T[r][0] == '#':
        #     dp[r][0] += 1
    # p(dp)

    for r in range(1, H):
        for c in range(1, W):
            from_up = dp[r - 1][c]
            if T[r - 1][c] == '.' and T[r][c] == '#':
                from_up += 1

            from_left = dp[r][c - 1]
            if T[r][c - 1] == '.' and T[r][c] == '#':
                from_left += 1

            dp[r][c] = min(from_up, from_left)

            # if r == H - 1 and c == W - 1 and T[r][c] == '#':
            #     dp[r][c] += 1

    # p(dp)
    print(dp[H - 1][W - 1])


main()
