import sys
import math
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    M = set()
    ct = 0
    # for i in range(2, N + 1):
    for i in range(2, int(math.sqrt(N)) + 1):
        j = 2
        while True:
            v = i**j
            if v > N:
                break
            j += 1
            if v in M:
                continue
            else:
                ct += 1
                M.add(v)

    print(N - ct)


main()
