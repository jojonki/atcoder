def read_int_list():
    return list(map(int, input().split()))


def main():
    N = int(input())
    A = read_int_list()
    A.sort()
    print(A[-1] - A[0])


main()
