import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


memo = {}


def f(v, N):
    # print()
    if v in memo:
        return memo[v]

    a = N
    b = v - N
    if b <= 0:
        a -= (1 - b)
        b = 1
    ct = max(0, a - b + 1)

    memo[v] = ct
    return memo[v]


def main():
    global memo
    N, K = read_ints()
    ans = 0
    L = 2 * N
    M = 2 * N - K
    while L >= 2 and M >= 2:
        ans += f(L, N) * f(M, N)
        L -= 1
        M -= 1

    print(ans)


main()
