import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import Counter


def main():
    N = int(input())
    A = read_int_list()
    c = []
    for a in A:
        c.append(a)
        c.append(a + 1)
        c.append(a - 1)
    c = Counter(c)
    print(c.most_common()[0][1])


main()
