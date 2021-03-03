import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = read_int_list()
    x = []
    sign = 1
    x0 = 0
    for a in A:
        x0 += sign * a
        sign *= -1
    x.append(x0)
    for i, a in enumerate(A[:-1]):
        x.append(2 * a - x[i])
    print(*x)


main()
