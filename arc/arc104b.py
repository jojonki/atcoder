import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def main2():
    N, S = input().split()
    N = int(N)
    ans = 0
    M = {
        'A': [0] * (N + 1),
        'T': [0] * (N + 1),
        'C': [0] * (N + 1),
        'G': [0] * (N + 1),
    }
    for i, c in enumerate(S):
        for k in ['A', 'T', 'C', 'G']:
            M[k][i + 1] = M[k][i]
        M[c][i + 1] += 1

    for i in range(N):
        for j in range(i + 1, N + 1):
            if (j - i) % 2 == 1: continue
            A_ct = M['A'][j] - M['A'][i]
            T_ct = M['T'][j] - M['T'][i]
            C_ct = M['C'][j] - M['C'][i]
            G_ct = M['G'][j] - M['G'][i]
            if A_ct == T_ct and C_ct == G_ct:
                ans += 1
    print(ans)


def main():
    N, S = input().split()
    N = int(N)
    ans = 0
    for i in range(N):
        c1, c2 = 0, 0
        for j in range(i, N):
            if S[j] == 'A':
                c1 += 1
            elif S[j] == 'T':
                c1 -= 1
            elif S[j] == 'C':
                c2 += 1
            elif S[j] == 'G':
                c2 -= 1
            if c1 == 0 and c2 == 0:
                ans += 1
    print(ans)


main()
