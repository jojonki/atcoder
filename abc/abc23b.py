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
    m = 'b'
    if S == m:
        print(0)
        return
    ct = 1

    while len(m) <= N:
        if ct % 3 == 1:
            m = 'a' + m + 'c'
        elif ct % 3 == 2:
            m = 'c' + m + 'a'
        elif ct % 3 == 0:
            m = 'b' + m + 'b'
        if m == S:
            print(ct)
            return
        ct += 1

    print(-1)


main()
