import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


MOD = int(1e9) + 7


def p(n):
    ans = 1
    for v in range(1, n + 1):
        ans = ans * v
        ans = ans % MOD
    return ans


def main():
    N, M = read_ints()
    if N == M:
        tmp = p(N)
        print((tmp * tmp * 2) % MOD)
    elif abs(N - M) == 1:
        print((p(N) * p(M)) % MOD)
    else:
        print(0)


main()
