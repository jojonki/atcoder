def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N_str = input()
    N = int(N_str)
    if N % sum([int(d) for d in N_str]) == 0:
        print('Yes')
    else:
        print('No')


main()
