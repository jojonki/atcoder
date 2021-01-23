def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = int(input())
    amari = N % 500
    if amari <= A:
        print('Yes')
    else:
        print('No')


main()
