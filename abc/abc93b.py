def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B, K = read_ints()
    if B - A + 1 <= 2 * K:
        for i in range(A, B + 1):
            print(i)
    else:
        for i in range(K):
            print(A + i)

        for i in range(K):
            print(B - K + i + 1)


main()
