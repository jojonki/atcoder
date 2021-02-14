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
    ans = 1
    cur = A[0]
    up = None
    for a in A[1:]:
        if cur == a:
            continue
        if a > cur:
            if up is not None and up is False:
                ans += 1
                up = None
            else:
                up = True
        else:
            if up is not None and up is True:
                ans += 1
                up = None
            else:
                up = False
        cur = a
    print(ans)


main()
