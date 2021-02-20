import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import ceil, floor


def f(n, x):
    # 0以上n以下の整数の内，xで割り切れる整数の数を返す
    if n < 0:
        return 0

    return n // x + 1


def main():
    a, b, x = read_ints()
    left = f(b, x)
    right = f(a - 1, x)
    print(left - right)


main()
