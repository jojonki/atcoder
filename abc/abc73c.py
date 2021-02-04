import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = set()
    for _ in range(N):
        a = int(input())
        if a in A:
            A.remove(a)
        else:
            A.add(a)
    print(len(A))


main()
