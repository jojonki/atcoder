def main():
    N, X, T = map(int, input().split())
    res = 0
    ct = 0
    while N > ct:
        ct += X
        res += T
    print(res)


main()
