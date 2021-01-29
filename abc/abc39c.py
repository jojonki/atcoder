import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


map = ['Do', '', 'Re', '', 'Mi', 'Fa', '', 'So', '', 'La', '', 'Si']


def main():
    S = input()
    kenban = 'WBWBWWBWBWBW' * 2  # 12
    offset = kenban.find(S[0:12])
    print(map[offset])


main()
