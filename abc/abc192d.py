import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import pow, ceil, sqrt, floor

X = [int(v) for v in list(input())]  # 234 = [2, 3, 4]
M = int(input())
N = len(X)
d = max(X)


def check(n):
    # decimalをn進法で表したときの値
    # decimal: int, n:int
    S = 0
    for d in X:
        S = S * n + d
        if S > M:
            break

    return S <= M


def check1(n):
    # n進数
    S = 0
    for i, digit in enumerate(X):
        try:
            S += pow(n, N - 1 - i) * digit
            # S += pow(n, i) * digit
        except OverflowError:
            S = M + 1
            break

        if S > M:
            break
    return S <= M


def main():
    if N == 1:
        if X[0] <= M:
            print(1)
        else:
            print(0)
        return

    if not check(d + 1):
        print(0)
        return

    ok = d
    ng = M + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        # print(ok, mid, ng)
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok - d)


main()
