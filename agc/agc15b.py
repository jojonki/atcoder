import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


# from itertools import permutations


def main():
    S = list(input())
    N = len(S)
    ans = 0
    for i, s in enumerate(S):
        # forward
        if s == 'U':
            ans += (N - 1 - i)  # forward
            ans += i * 2  # backward
        else:
            ans += (N - 1 - i) * 2  # forward
            ans += i  # backward

    print(ans)


main()
