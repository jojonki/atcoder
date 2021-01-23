def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    print(min(A, B) + min(C, D))


main()
