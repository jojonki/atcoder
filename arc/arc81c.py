import sys
from typing import DefaultDict
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
    counter = defaultdict(int)
    counter2 = {}
    for a in A:
        counter[a] += 1

    for a, ct in counter.items():
        if ct >= 2:
            counter2[a] = ct
    counter2 = sorted(counter2.items(), key=lambda x: -x[0])
    ans = 0
    i = 0
    for a, ct in counter2:
        if i == 0:
            if ct >= 4:
                print(a * a)
                return
            else:
                ans = a
        elif i == 1:
            print(ans * a)
            return
        else:
            print(0)
            return

        i += 1
    print(0)


main()
