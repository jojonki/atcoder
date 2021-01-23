def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, A, B = read_ints()
    print(min(A * N, B))


main()
