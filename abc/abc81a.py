def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    ans = 0
    for c in input():
        if c == '1':
            ans += 1
    print(ans)


main()
