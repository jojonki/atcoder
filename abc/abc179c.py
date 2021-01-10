def main_tle():
    N = int(input())
    res = 0
    for c in range(1, N):
        ab = N - c
        # print('c=', c, ', ab=', ab)
        i = 1
        while i * i <= ab:
            if ab % i == 0:
                j = ab // i
                if i == j:
                    # print(i, j)
                    res += 1
                else:
                    # print(i, j)
                    # print(j, i)
                    res += 2

            i += 1
    print(res)


def main():
    N = int(input())
    res = 0
    for a in range(1, N):
        res += (N - 1) // a
    print(res)


main()
