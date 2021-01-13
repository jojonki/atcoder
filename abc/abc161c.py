def main():
    N, K = map(int, input().split())
    N = min(N, N % K)
    # print(N)
    print(min(abs(N), abs(N - K)))


main()
