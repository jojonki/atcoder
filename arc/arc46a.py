import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    ct = 1
    keta = 1
    while True:
        for i in range(1, 10):
            if ct == N:
                v = str(i) * keta
                print(v)
                return
            ct += 1
        keta += 1


main()
