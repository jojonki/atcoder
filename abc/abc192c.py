import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def f(v):
    v = list(str(v))
    v.sort()
    return int(''.join(v[::-1])) - int(''.join(v))


def main():
    N, K = read_ints()
    v = N
    for _ in range(K):
        v = f(v)
    print(v)


main()
