import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = input()
    N = int(input())
    for _ in range(N):
        l, r = read_ints()
        l -= 1
        r -= 1
        S = S[:l] + S[l:r + 1][::-1] + S[r + 1:]
    print(S)


main()
