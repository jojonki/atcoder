def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(M):
        N -= A[i]
    if N < 0:
        print(-1)
    else:
        print(N)


main()
