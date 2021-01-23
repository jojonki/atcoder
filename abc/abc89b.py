def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    for s in input().split():
        if s == 'Y':
            print('Four')
            return

    print('Three')


main()
