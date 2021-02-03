import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def main():
    N = int(input())
    A = read_int_list()

    any_ct = 0
    C = defaultdict(int)
    for a in A:
        if a <= 399:
            C['Gray'] += 1
        elif a <= 799:
            C['Brown'] += 1
        elif a <= 1199:
            C['Green'] += 1
        elif a <= 1599:
            C['Water'] += 1
        elif a <= 1999:
            C['Blue'] += 1
        elif a <= 2399:
            C['Yellow'] += 1
        elif a <= 2799:
            C['Orange'] += 1
        elif a <= 3199:
            C['Red'] += 1
        else:
            any_ct += 1

    fixed_cols = len(C.keys())
    max_cols = fixed_cols + any_ct
    if fixed_cols == 0:
        min_cols = 1
    else:
        min_cols = fixed_cols
    print(min_cols, max_cols)


main()
