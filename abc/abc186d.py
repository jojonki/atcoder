def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    # S = 0
    # SA = []
    # for a in A:
    #     S += a
    #     SA.append(S)
    # res = 0
    # for i in range(N - 1):
    #     res += (S - SA[i] - (N - 1 - i) * A[i])
    # print(res)

    ans = 0
    SA = 0
    for j in range(N):
        ans += A[j] * j
        ans -= SA
        SA += A[j]
    print(ans)


main()
