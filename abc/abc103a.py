def main():
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    ans = 0
    for i in range(1, len(A)):
        ans += abs(A[i] - A[i - 1])
    print(ans)


main()
