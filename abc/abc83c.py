def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    X, Y = read_ints()
    ans = 1
    v = X * 2
    while v <= Y:
        ans += 1
        v *= 2
    print(ans)


main()
