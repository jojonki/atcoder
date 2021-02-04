import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = read_ints()
    n_four = 0
    n_two = 0
    n_others = 0
    for a in A:
        if a % 4 == 0:
            n_four += 1
        elif a % 2 == 0:
            n_two += 1
        else:
            n_others += 1
    if n_four * 2 + 1 >= N:
        print('Yes')
    else:
        if n_four + 1 >= min(1, n_two) + n_others:
            print('Yes')
        else:
            print('No')


main()
