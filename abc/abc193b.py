import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    ans = INF
    for _ in range(N):
        A, P, X = read_ints()
        X -= A
        # print(X)
        if X > 0:
            ans = min(ans, P)
    if ans == INF:
        print(-1)
    else:
        print(ans)


main()
