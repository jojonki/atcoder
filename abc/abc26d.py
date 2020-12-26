import math

eps = 1e-6


def f(A, B, C, t):
    return A * t + B * math.sin(C * math.pi * t)


def main():
    A, B, C = map(int, input().split())
    l, r = 0, 1000
    while l < r:
        t = (l + r) / 2
        v = f(A, B, C, t)
        if abs(v - 100) <= eps:
            print(t)
            break
        elif v < 100:
            l = t
        else:
            r = t


main()
