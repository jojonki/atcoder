import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    S = input()
    ans = 0
    for c in S:
        if c == 'A':
            ans += 4
        elif c == 'B':
            ans += 3
        elif c == 'C':
            ans += 2
        elif c == 'D':
            ans += 1
    print(ans / N)


main()
