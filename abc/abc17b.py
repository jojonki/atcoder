import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = input()
    if S == '':
        print('Yes')

    i = 0
    while i < len(S):
        c = S[i]
        if c == 'o' or c == 'k' or c == 'u':
            i += 1
            continue
        elif c == 'c':
            if i < len(S) - 1 and S[i + 1] == 'h':
                i += 2
                continue
            else:
                # print('---------', i, c)
                print('NO')
                return
        else:
            # print('---------', i, c)
            print('NO')
            return
    print('YES')


main()
