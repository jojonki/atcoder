def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    a, b = read_ints()
    diff = b - a
    x = 1
    for i in range(2, 1001):
        y = x + i
        if y - x == diff:
            print(y - b)
            return
        x = y


main()
