from math import floor, ceil


def calc2(A, B, x):
    # 式変形すると得られる
    return floor(A * (x % B) / B)


def calc(A, B, x):
    return floor(A * x / B) - A * floor(x / B)


def main():
    A, B, N = map(int, input().split())
    x = min(N, B - 1)
    print(calc(A, B, x))


main()
