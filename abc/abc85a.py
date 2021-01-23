def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = input()
    S = S.replace('2017', '2018')
    print(S)


main()
