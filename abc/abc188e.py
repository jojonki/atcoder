from collections import defaultdict as dd


def main_morau():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    come_from = dd(list)
    for _ in range(M):
        a, b = map(int, input().split())
        come_from[b - 1].append(a - 1)

    dp = [float('inf') for _ in range(N)]
    ans = -float('inf')
    for i in range(N):
        for j in come_from[i]:
            dp[i] = min(
                dp[i],
                dp[j],
                A[j],
            )
        ans = max(ans, A[i] - dp[i])
    print(ans)


def main_kubaru():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    to = dd(list)
    for _ in range(M):
        a, b = map(int, input().split())
        to[a - 1].append(b - 1)

    dp = [float('inf') for _ in range(N)]
    ans = -float('inf')
    for i in range(N):
        for j in to[i]:
            dp[j] = min(
                dp[j],
                dp[i],
                A[i],
            )
        ans = max(ans, A[i] - dp[i])
    print(ans)


main_kubaru()
# main_morau()
