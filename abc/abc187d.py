def main():
    N = int(input())
    D = []
    aoki = 0
    for _ in range(N):
        a, b = map(int, input().split())
        aoki += a
        D.append((a, b))
    # D.sort(key=lambda x: x[1] - x[0])
    # D.sort(key=lambda x: -x[1])
    D.sort(key=lambda x: -(2 * x[0] + x[1]))
    # print(D)
    takahashi = 0
    for i, (a, b) in enumerate(D):
        aoki -= a
        takahashi += a + b
        if aoki < takahashi:
            print(i + 1)
            return


main()
