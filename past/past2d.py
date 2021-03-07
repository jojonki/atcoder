import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from itertools import product


def main():
    # S = list(input())
    S = input()
    # unique_chars = len(set(S))
    sub = set()

    for win_size in range(1, 4):
        for i in range(len(S) - win_size + 1):
            s = S[i:i + win_size]
            for bit in range(1 << 3):
                tmp_s = ''
                for s_i, s_c in enumerate(s):
                    if bit >> (len(s) - s_i - 1) & 1 == 1:
                        tmp_s += '.'
                    else:
                        tmp_s += s_c
                # print(bit, tmp_s)
                sub.add(tmp_s)

    print(len(sub))

    # print(ans)


main()
