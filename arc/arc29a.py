import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from itertools import product


def main_zentansaku():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    D = [('A', 'B')] * N
    ans = INF
    for p in product(*D):
        g1, g2 = 0, 0
        for i, g in enumerate(p):
            if g == 'A':
                g1 += T[i]
            else:
                g2 += T[i]
        ans = min(ans, max(g1, g2))
    print(ans)


def main_big():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    total = sum(T)
    ans = INF

    for bit in range(1 << N):
        tmp = 0
        for i in range(N):
            if bit & 1 << i:
                tmp += T[i]
        ans = min(ans, max(tmp, total - tmp))
    print(ans)


def main_dfs():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    total = sum(T)
    global ans
    ans = INF

    def dfs(i, tmp):
        global ans
        # tmp: グリルAの必要焼き時間，グリルBの必要焼き時間はtotal-tmp
        if i == N:
            # グリルA,Bの長いほうが必要焼き時間
            # print(ans, max(tmp, total - tmp))
            ans = min(ans, max(tmp, total - tmp))
        else:
            dfs(i + 1, tmp)  # Bで焼いてもらう
            dfs(i + 1, tmp + T[i])  # Aで焼く

    dfs(0, 0)
    print(ans)


main_dfs()
