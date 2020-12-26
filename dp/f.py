S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        if S[i - 1] == T[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print(dp)
# for sdp in dp:
#     print(sdp)

subs = ''
subs_len = dp[-1][-1]
i, j = len(S), len(T)
while i > 0 and j > 0:
    if S[i - 1] == T[j - 1]:
        subs += S[i - 1]
        i -= 1
        j -= 1
    elif dp[i - 1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1
print(subs[::-1])
