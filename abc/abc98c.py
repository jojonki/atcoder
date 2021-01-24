def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    S = list(input())
    W, E = [0] * N, [0] * N
    for i in range(N):
        if S[i] == 'W':
            if i == 0:
                W[i] = 1
            else:
                W[i] = W[i - 1] + 1
        else:  # S[i]==E
            if i == 0:
                W[i] = 0
            else:
                W[i] = W[i - 1]

        k = N - 1 - i
        if S[k] == 'E':
            if k == N - 1:
                E[k] = 1
            else:
                E[k] = E[k + 1] + 1
        else:  # E[k] == W
            if k == N - 1:
                E[k] = 0
            else:
                E[k] = E[k + 1]
    ans = float('inf')
    for i in range(N):
        if i == 0:
            ans = min(ans, E[i + 1])
        elif i == N - 1:
            ans = min(ans, W[i - 1])
        else:
            ans = min(ans, W[i - 1] + E[i + 1])
    # print(W)
    # print(E)
    print(ans)


main()
