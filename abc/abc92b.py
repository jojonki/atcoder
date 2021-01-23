def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    D, X = read_ints()
    ct = 0
    for _ in range(N):
        a = int(input())
        d = 1
        ct += 1
        while d + a <= D:
            ct += 1
            d += a
    print(ct + X)


main()
