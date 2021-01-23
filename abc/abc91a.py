def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B, C = read_ints()
    if C <= A + B:
        print('Yes')
    else:
        print('No')


main()
