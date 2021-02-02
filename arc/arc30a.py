import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    n = int(input())
    k = int(input())
    # if k == 1:
    #     print('YES')
    #     return
    if k <= n // 2:
        print('YES')
    else:
        print('NO')


main()
