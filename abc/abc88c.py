def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    c11, c12, c13 = read_int_list()
    c21, c22, c23 = read_int_list()
    c31, c32, c33 = read_int_list()

    if c11-c12 == c21-c22 == c31-c32 and \
        c12-c13 == c22-c23 == c32-c33 and \
            c11-c21 == c12-c22 == c13-c23 and\
                c21-c31 == c22-c32 == c23-c33:
        print('Yes')
    else:
        print('No')

    # print(C)


main()
