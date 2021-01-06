def main():
    H, W = map(int, input().split())
    d = []
    min_v = float('inf')
    for i in range(H):
        w = list(map(int, input().split()))
        for v in w:
            if v < min_v:
                min_v = v
            d.append(v)
    res = 0
    for v in d:
        res += (v - min_v)

    print()


main()
