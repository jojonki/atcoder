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

    u = sorted(list(set(A)))
    if len(u) == 1:
        if A[0] == 0:
            print('Yes')
        else:
            print('No')
    elif len(u) == 2:
        if A.count(0) == N // 3:
            print('Yes')
        else:
            print('No')
    elif len(u) == 3:
        if A.count(u[0]) == A.count(u[1]) == A.count(u[2]) == N // 3:
            if u[0] ^ u[1] ^ u[2] == 0:
                print('Yes')
                return
        print('No')
    else:
        print('No')


main()
