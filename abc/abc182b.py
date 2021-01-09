import math


def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_gcd = 0
    res = None
    max_v = max(A)
    for v in range(2, max_v + 1):
        gcd = 0
        for a in A:
            if a % v == 0:
                gcd += 1
        if gcd > max_gcd:
            max_gcd = gcd
            res = v
    print(res)


main()
