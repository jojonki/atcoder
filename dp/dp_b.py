def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, K = read_ints()
    H = read_int_list()
    dp = [float('INF')] * N
    dp[0] = 0
    for i in range(N - 1):
        for j in range(1, K + 1):
            # i -> i+j
            if i + j < N:
                dp[i + j] = min(dp[i] + abs(H[i + j] - H[i]), dp[i + j])
            else:
                break
    print(dp[N - 1])


main()
