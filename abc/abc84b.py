def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B = read_ints()
    S = input().split('-')
    if len(S) != 2:
        print('No')
        return

    if len(S[0]) == A and len(S[1]) == B:
        print('Yes')
    else:
        print('No')


main()
