def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    a, b, c, d = read_ints()
    if abs(c - a) <= d:
        print('Yes')
    elif abs(b - a) <= d and abs(c - b) <= d:
        print('Yes')
    else:
        print('No')


main()
