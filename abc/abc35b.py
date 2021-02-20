import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = input()
    T = int(input())
    V, H = 0, 0
    wild = 0
    for c in S:
        if c == 'U':
            V += 1
        elif c == 'D':
            V -= 1
        elif c == 'L':
            H -= 1
        elif c == 'R':
            H += 1
        else:
            wild += 1

    d = abs(V) + abs(H)
    if T == 1:  # maximize
        d += wild
        print(d)
    else:  # minimize
        for _ in range(wild):
            if d > 0:
                d -= 1
            else:
                d += 1
        print(d)


main()
