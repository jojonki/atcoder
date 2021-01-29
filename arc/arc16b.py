import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    ans = 0
    pressed = [False] * 9
    for _ in range(N):
        for i, c in enumerate(input()):
            if c == 'x':
                ans += 1
            elif c == 'o':
                if pressed[i] is False:
                    ans += 1
                    pressed[i] = True
            if pressed[i] is True and c in ['.', 'x']:
                pressed[i] = False
    print(ans)


main()
