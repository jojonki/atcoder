import math


def main():
    N = int(input())
    x = list(map(int, input().split()))
    m, u = 0, 0
    max_v = -float('inf')
    for v in x:
        m += abs(v)
        u += abs(v) * abs(v)
        max_v = max(abs(v), max_v)
    print(m)
    print(math.sqrt(u))

    print(max_v)


main()
