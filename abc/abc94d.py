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
    A.sort()

    aj = A[-1]
    ak = A[-2]
    cur_max = min(ak, aj - ak)
    for a in A[:-2]:
        val = min(a, aj - a)
        if cur_max < val:
            ak = a
            cur_max = val
    print(aj, ak)


main()
