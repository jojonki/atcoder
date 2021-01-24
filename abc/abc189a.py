def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = set(list(input()))
    if len(S) == 1:
        print('Won')
    else:
        print('Lost')


main()
