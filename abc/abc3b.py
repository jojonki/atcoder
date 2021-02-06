import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S, T = input(), input()
    atcoder = list('atcoder')
    Win = True
    for c1, c2 in zip(S, T):
        if c1 == c2:
            continue
        elif c1 == '@' and c2 in atcoder:
            continue
        elif c2 == '@' and c1 in atcoder:
            continue
        else:
            Win = False
    if Win:
        print('You can win')
    else:
        print('You will lose')


main()
