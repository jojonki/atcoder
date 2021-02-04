import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import Counter


def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(input())
    A = Counter(A)
    print(A.most_common()[0][0])


main()
