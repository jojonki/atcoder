def main():
    N, C = map(int, input().split())
    usage = {}
    res = 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        if a not in usage:
            usage[a] = 0
        if b + 1 not in usage:
            usage[b + 1] = 0

        usage[a] += c
        usage[b + 1] -= c

    T = list(usage.keys())
    T.sort()

    S = [0]
    for t in T:
        S.append(S[-1] + usage[t])
        # print('t=', t, ',p=', usage[t], ',S=', S[-1])
    # print('T', T)
    # print('S', S)

    for i in range(1, len(T)):
        duration = T[i] - T[i - 1]
        price = min(C, S[i])
        # print('i=', i, 'p=', price, '*', duration)
        res += price * duration

    print(res)


main()
