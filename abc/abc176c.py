def main():
    N = int(input())
    A = list(map(int, input().split()))
    min_h = 0
    res = 0
    for h in A:
        if h < min_h:
            res += (min_h - h)
        min_h = max(min_h, h)
    print(res)


main()
