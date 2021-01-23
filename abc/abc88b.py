def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    input()
    A = read_int_list()
    A.sort(reverse=True)
    alice, bob = 0, 0
    for i in range(len(A)):
        if i % 2 == 0:
            alice += A[i]
        else:
            bob += A[i]
    print(alice - bob)


main()
