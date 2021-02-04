import sys
from itertools import product
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    cs = ['a', 'b', 'c']
    for v in product(cs, repeat=N):
        print(''.join(v))


main()
