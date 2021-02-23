import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import ceil


def main():
    N = int(input())
    C, S, F = [], [], []
    for _ in range(N - 1):
        c, s, f = read_ints()
        C.append(c)
        S.append(s)
        F.append(f)

    for i in range(N - 1):
        cur_time = S[i] + C[i]
        for j in range(i + 1, N - 1):
            n = max(0, ceil(cur_time / F[j]) - S[j] / F[j])
            cur_time = int(S[j] + n * F[j]) + C[j]
        print(cur_time)
    print(0)


main()
