def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, M = read_ints()
    ans = (1900 * M) * (2**M) + 100 * (N - M) * (2**M)
    print(ans)


main()
