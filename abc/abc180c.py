def main():
    N = int(input())
    i = 1
    res = []
    while i * i <= N:
        if N % i == 0:
            j = N // i
            if i == j:
                res.append(i)
            else:
                res.append(i)
                res.append(j)
        i += 1
    # print(N)
    res.sort()
    for v in res:
        print(v)


main()
