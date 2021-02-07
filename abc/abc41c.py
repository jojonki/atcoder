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
    R = {}
    for i, a in enumerate(A):
        R[a] = i + 1
    A.sort(reverse=True)
    for a in A:
        print(R[a])


main()
