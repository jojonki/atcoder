def main():
    ans = float('inf')
    N, M, X = map(int, input().split())
    C, A = [], []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        c, a = tmp[0], tmp[1:]
        C.append(c)
        A.append(a)

    for b in range(1 << N):  # for all buying patterns
        d = [0] * M
        cost = 0
        for i in range(N):
            if (b >> i) & 1 == 1:
                for j, a in enumerate(A[i]):
                    d[j] += a
                cost += C[i]
        if all([v >= X for v in d]):
            ans = min(ans, cost)
        # print(format(b, 'b'))
    if ans == float('inf'):
        ans = -1
    print(ans)


main()
