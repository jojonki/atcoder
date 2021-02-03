import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a - 1)
    M = set()
    on = 0
    M.add(on)
    # print(A)
    for i in range(N):
        on = A[on]
        if on in M:
            print(-1)
            return
        if on == 1:
            print(i + 1)
            return
    print(-1)


main()
