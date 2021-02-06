import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = input()
    cands = []
    for i in range(16):
        s = S
        a0, a1, a2, a3 = '', '', '', ''
        if i & (1 << 0):
            a0 = 'A'
        if i & (1 << 1):
            a1 = 'A'
        if i & (1 << 2):
            a2 = 'A'
        if i & (1 << 3):
            a3 = 'A'
        s = a3 + 'KIH' + a2 + 'B' + a1 + 'R' + a0
        cands.append(s)
    # print(cands)
    if S in cands:
        print('YES')
    else:
        print('NO')


main()
