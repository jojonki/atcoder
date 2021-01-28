def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = list(input())
    if len(set(N[:3])) == 1 or len(set(N[1:4])) == 1:
        print('Yes')
    else:
        print('No')


main()
