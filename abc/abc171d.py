from collections import defaultdict as dd


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    S = 0
    memo = dd(int)
    for a in A:
        S += a
        memo[a] += 1

    for _ in range(Q):
        b, c = map(int, input().split())
        S += (c - b) * memo[b]
        print(S)

        memo[c] += memo[b]
        memo[b] = 0


main()
