N = int(input())
H = []
for _ in range(N):
    a, b, c = map(int, input().split())
    H.append([a, b, c])

dp = [[float('inf')] * 3 for _ in range(N+1)]
dp[0] = [0, 0, 0]
for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + H[i-1][0] 
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + H[i-1][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + H[i-1][2]
print(max(dp[N]))

