def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, M, X = read_ints()
    A = read_int_list()
    L, R = 0, 0
    for i, a in enumerate(A):
        if a < X:
            L += 1
        elif a > X:
            R += 1
    print(min(L, R))


main()
