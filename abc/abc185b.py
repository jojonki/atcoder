def main():
    N, M, T = map(int, input().split())
    C = N
    t = 0
    for _ in range(M):
        if N <= 0:
            print('No')
            return
        a, b = map(int, input().split())
        N -= (a - t)
        if N <= 0:
            print('No')
            return
        N = min(C, N + (b - a))
        t = b
    N -= (T - t)
    if N <= 0:
        print('No')
        return

    print('Yes')


main()
