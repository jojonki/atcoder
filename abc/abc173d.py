def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0]
    for i in range(2, N):
        ans += A[i // 2]
    print(ans)


main()
