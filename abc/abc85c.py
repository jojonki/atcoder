def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def f(a, b, c):
    # print('price=', 10000 * a + 5000 * b + 1000 * c)
    print(a, b, c)


def main():
    N, Y = read_ints()

    for a in range(2001):
        for b in range(2001):
            c = N - (a + b)
            if c < 0:
                break
            if 10000 * a + 5000 * b + 1000 * c == Y:
                f(a, b, c)
                return
    print(-1, -1, -1)


main()
