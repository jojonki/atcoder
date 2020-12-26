# N = int(input())
# H = list(map(int, input().split()))
# dp = [0]
# if N == 1:
#     print(0)
# else:
#     dp.append(dp[0] + abs(H[1]-H[0])) # step-1
#     for i in range(2, N):
#         c_one_step = dp[i-1] + abs(H[i] - H[i-1])
#         c_two_step = dp[i-2] + abs(H[i] - H[i-2])
#         dp.append(min(c_one_step, c_two_step))

#     print(dp[-1])

# 12/26
N = int(input())
H = list(map(int, input().split()))

dp = [float('inf')] * (N)
dp[0] = 0

for i in range(1, N):
    one_step = dp[i - 1] + abs(H[i] - H[i - 1])
    if i > 1:
        two_step = dp[i - 2] + abs(H[i] - H[i - 2])
    else:
        two_step = float('inf')
    dp[i] = min(one_step, two_step)

print(dp[-1])
