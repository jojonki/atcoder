def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B, C, X, Y = read_ints()
    ans = 0
    if A + B <= 2 * C:
        ans += A * X + B * Y
    else:
        ans += min(X, Y) * (2 * C)
        if X < Y:
            if B < 2 * C:
                ans += (Y - X) * B
            else:
                ans += (Y - X) * (2 * C)
        else:
            if A < 2 * C:
                ans += (X - Y) * A
            else:
                ans += (X - Y) * (2 * C)
    print(ans)


main()
