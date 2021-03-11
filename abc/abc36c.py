import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


import copy


def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    B = list(set(copy.copy(A)))
    B.sort()
    # print(B)
    C = {}
    for i, b in enumerate(B):
        C[b] = i

    for i in range(N):
        print(C[A[i]])


main()
