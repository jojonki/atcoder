def main():
    N, R = map(int, input().split())
    res = R
    if N >= 10:
        pass
    else:
        res = res + 100 * (10 - N)
    print(res)


main()
