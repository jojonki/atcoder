M = int(1e9) + 7


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [A[-1]]
    for i in range(1, N - 1):
        v = A[N - 1 - i]
        S.append(S[-1] + v)
    S = S[::-1]
    res = 0
    # print('A;', A)
    # print('S;', S)
    for i in range(N - 1):
        # print('i=', i, A[i], '*', S[i])
        res = (res + (A[i] % M) * (S[i] % M)) % M
    print(res)

    # print()
    # # A = [141421356, 17320508, 22360679, 244949]
    # N = len(A)
    # res = 0
    # for i in range(N - 1):
    #     for j in range(i + 1, N):
    #         print(A[i], '*', A[j])
    #         res += A[i] * A[j]

    # print(res % M)


main()
