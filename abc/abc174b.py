from math import sqrt


def main():
    N, D = map(int, input().split())
    res = 0
    for _ in range(N):
        x, y = map(int, input().split())
        d = sqrt(x * x + y * y)
        if d <= D:
            res += 1

    print(res)


main()
