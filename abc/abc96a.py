def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    a, b = read_ints()
    ans = 0
    for i in range(1, 13):
        if i < a:
            ans += 1
        elif i == a and i <= b:
            ans += 1
        else:
            break
    print(ans)


main()
