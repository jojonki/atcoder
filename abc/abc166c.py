def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    ng = set()
    for i in range(M):
        a, b = map(int, input().split())
        ha, hb = H[a - 1], H[b - 1]
        if ha > hb:
            ng.add(b)
        elif ha < hb:
            ng.add(a)
        else:
            ng.add(a)
            ng.add(b)
    print(N - len(ng))


main()
