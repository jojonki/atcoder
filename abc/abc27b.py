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
    P = sum(A)
    if P % N != 0:
        print(-1)
    else:
        p = P // N
        ans = 0
        cur = 0
        for a in A:
            cur += (p - a)
            if cur != 0:
                ans += 1
        print(ans)


main()
