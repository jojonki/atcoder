import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, K = read_ints()
    G = 2 * (10**12)
    ans = 0
    if K == 0:
        ans = G - A

    else:
        while A < G:
            A += 1 + K * A
            ans += 1
    print(ans)


main()
