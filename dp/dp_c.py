def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    dp = [[0, 0, 0] for _ in range(N)]
    A = []
    for _ in range(N):
        A.append(read_int_list())

    dp[0][0] = A[0][0]
    dp[0][1] = A[0][1]
    dp[0][2] = A[0][2]

    for i in range(1, N):
        for j in range(3):
            happy = A[i][j]
            act1 = (j + 1) % 3
            act2 = (j + 2) % 3
            dp[i][j] = max(dp[i - 1][act1], dp[i - 1][act2]) + happy
    print(max(dp[N - 1]))


main()
