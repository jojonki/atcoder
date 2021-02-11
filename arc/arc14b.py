import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    M = set()

    turn = True
    last = ''
    for _ in range(N):
        w = input()
        if w in M:
            if turn:
                print('LOSE')
            else:
                print('WIN')
            return
        if last and last[-1] != w[0]:
            if turn:
                print('LOSE')
            else:
                print('WIN')
            return

        M.add(w)
        turn = not turn
        last = w
    print('DRAW')


main()
