import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    ans = 0
    P = read_int_list()
    i = 0
    while i < N:
        if i + 1 == P[i]:
            if i < N - 1 and i + 2 == P[i + 1]:
                ans += 1
                i += 2
                continue
            else:
                ans += 1
        i += 1

    print(ans)


main()
