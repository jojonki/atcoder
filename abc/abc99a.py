def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    if N <= 999:
        print('ABC')
    else:
        print('ABD')


main()
