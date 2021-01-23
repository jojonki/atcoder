def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B, X = read_ints()
    if B >= (X - A) >= 0:
        print('YES')
    else:
        print('NO')


main()
