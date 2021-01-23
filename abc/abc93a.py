def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = input()
    if 'a' in S and 'b' in S and 'c' in S:
        print('Yes')
    else:
        print('No')


main()
