def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B, C, D = read_ints()
    L, R = A + B, C + D
    if L == R:
        print('Balanced')
    elif L > R:
        print('Left')
    else:
        print('Right')


main()
