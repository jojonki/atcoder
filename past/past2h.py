import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def p(table):
    for i in range(len(table)):
        print(table[i])


from collections import defaultdict, deque


def main_wa():
    H, W = read_ints()
    A = []
    s_r, s_c = None, None
    for r in range(H):
        row = []
        for c, char in enumerate(input()):
            if char == 'S':
                s_r = r
                s_c = c
                row.append(0)
            elif char == 'G':
                row.append(10)
            else:
                row.append(int(char))
        A.append(row)

    initial_cost = 0
    for goal in range(1, 11):
        q = deque([(s_r, s_c, initial_cost)])
        dp = [[INF] * W for _ in range(H)]
        dp[s_r][s_c] = initial_cost

        next_s_r, next_s_c, next_s_cost = None, None, INF
        while q:
            r, c, cost = q.popleft()
            if cost >= next_s_cost:
                continue
            # print(r, c, cost)
            if A[r][c] == goal:
                if cost < dp[r][c]:
                    dp[r][c] = cost
                    next_s_r = r
                    next_s_c = c
                    next_s_cost = cost
                continue

            if cost > dp[r][c]:
                continue
            else:
                dp[r][c] = cost
            # dp[r][c] = min(dp[r][c], cost)

            if r > 0:
                q.append((r - 1, c, cost + 1))
            if r < H - 1:
                q.append((r + 1, c, cost + 1))
            if c > 0:
                q.append((r, c - 1, cost + 1))
            if c < W - 1:
                q.append((r, c + 1, cost + 1))

        s_r, s_c, initial_cost = next_s_r, next_s_c, next_s_cost
        if initial_cost == INF:
            print(-1)
            return
        # print(f'goal={goal}, ({s_r}, {s_c}) cost={initial_cost}')
        # p(dp)
        # break

    print(next_s_cost)


from collections import defaultdict


def main():
    H, W = read_ints()
    A = []
    s_r, s_c = None, None
    M = defaultdict(list)
    for r in range(H):
        row = []
        for c, char in enumerate(input()):
            v = None
            if char == 'S':
                s_r = r
                s_c = c
                v = 0
            elif char == 'G':
                v = 10
            else:
                v = int(char)
            row.append(v)
            M[v].append((r, c))

        A.append(row)

    # cost[r][c] (r, c)での最小コスト
    cost = [[INF] * W for _ in range(H)]
    cost[s_r][s_c] = 0
    for goal in range(1, 11):  # 10
        start = goal - 1
        for s_r, s_c in M[start]:  # NM
            for g_r, g_c in M[goal]:  # NM
                dist = abs(g_r - s_r) + abs(g_c - s_c)
                cost[g_r][g_c] = min(cost[g_r][g_c], cost[s_r][s_c] + dist)

    ans = min([cost[r][c] for r, c in M[10]])
    if ans == INF:
        print(-1)
    else:
        print(ans)


main()
