def main():
    N, W = map(int, input().split())
    usage = [0]
    for _ in range(N):
        s, t, p = map(int, input().split())
        if t + 1 > len(usage):
            usage += [0] * (t + 1 - len(usage))
        usage[s] += p
        usage[t] -= p

    s = usage[0]
    if s > W:
        print('No')
        return
    for t in range(1, len(usage)):
        usage[t] += usage[t - 1]
        if usage[t] > W:
            print('No')
            return
    # print(usage)
    print('Yes')


main()
