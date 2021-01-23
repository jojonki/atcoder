def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, A, B = read_ints()
    ans = 0
    for v in range(1, N + 1):
        d = sum([int(c) for c in str(v)])
        if A <= d <= B:
            ans += v
    print(ans)


main()
