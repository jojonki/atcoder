def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    X = int(input())
    A = int(input())
    B = int(input())
    X -= A
    print(X % B)


main()
