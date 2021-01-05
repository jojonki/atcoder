def main():
    N = int(input())
    X = list(map(int, input().split()))
    P = round(sum(X) / N)
    res = 0
    for x in X:
        res += (x - P)**2

    print(res)


main()
