import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    M, D = read_ints()
    if M % D == 0:
        print('YES')
    else:
        print('NO')


main()
