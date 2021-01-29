import sys
sys.setrecursionlimit(1 << 20)


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict

# dp[v]: ノードvを始点にしたときの有効パスの最大長
dp = [-1] * 1000100
G = defaultdict(list)


def rec(v):
    # ノードvを始点にしたときの有効パスの最大長
    if dp[v] != -1:
        return dp[v]

    res = 0
    for nv in G[v]:
        res = max(res, rec(nv) + 1)
    dp[v] = res

    return dp[v]


def main():
    N, M = read_ints()

    for _ in range(M):
        frm, to = read_ints()
        frm -= 1
        to -= 1
        G[frm].append(to)

    # print(G)
    res = 0
    # 全ノードに対して，そのvを始点にしたときの最大長を求めていき，その最大値を答えとする
    for v in range(N):
        # vを始点にしたときのパス最大長
        res = max(res, rec(v))
    print(res)


main()
