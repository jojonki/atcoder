import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B, C = read_ints()
    while True:
        if C == 0:
            A -= 1
            if A <= 0:
                print('Aoki')
                return
            C = 1
        else:
            B -= 1
            if B <= 0:
                print('Takahashi')
                return
            C = 0


main()
