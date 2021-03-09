import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    W = []
    for _ in range(N):
        x, l = read_ints()
        begin, end = x - l, x + l
        W.append((begin, end))
    W.sort(key=lambda x: x[1])
    # print(W)
    ct = 0
    last_end = -INF
    for b, e in W:
        if last_end <= b:
            ct += 1
            last_end = e
    print(ct)


main()
