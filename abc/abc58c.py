import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = defaultdict(int)
        for c in input():
            s[c] += 1
        S.append(s)
    ans = []
    for char, ct in S[0].items():
        min_ct = ct
        for s in S[1:]:
            min_ct = min(min_ct, s[char])
            if min_ct == 0:
                break
        ans += [char] * min_ct
    ans.sort()
    print(''.join(ans))


main()
