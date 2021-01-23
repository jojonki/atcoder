def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    a, b = read_ints()
    if (a * b) % 2 == 0:
        print('Even')
    else:
        print('Odd')


main()
