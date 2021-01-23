def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B = read_ints()
    ans = 0
    for v in range(A, B + 1):
        s = str(v)
        if s == s[::-1]:
            ans += 1

    print(ans)


main()
