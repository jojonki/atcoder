def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    ans = 700
    for c in input():
        if c == 'o':
            ans += 100
    print(ans)


main()
