N, limitW = map(int, input().split())
W, V = [], []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)


dp = [[0 for _ in range(100001)] for _ in range(101)]

for i in range(N):
    for sumW in range(limitW + 1):
        score = dp[i][sumW]
        if W[i] <= sumW:
            score = max(score, dp[i][sumW-W[i]] + V[i])
        dp[i+1][sumW] = score
print(dp[N][limitW])