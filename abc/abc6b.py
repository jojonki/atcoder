import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    n = int(input())
    A = [0, 0, 1]
    for _ in range(3, n):
        A.append(sum(A[-3:]) % 10007)
    # print(A)
    print(A[n - 1])


main()
