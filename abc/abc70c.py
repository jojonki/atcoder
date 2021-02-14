import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def gcd(m, n):
    if n == 0:
        return m

    return gcd(n, m % n)


def lcm(a, b):
    # Least Common Multiple
    # a*b = gcd(a, b) * l
    # l = a / gcd(a, b) * b
    return a // gcd(a, b) * b


def main():
    N = int(input())
    T = []
    for _ in range(N):
        T.append(int(input()))
    # print(T)
    ans = None
    if len(T) <= 1:
        ans = T[0]
    else:
        ans = lcm(T[0], T[1])
        for t in T[2:]:
            ans = lcm(ans, t)
    print(ans)


main()
