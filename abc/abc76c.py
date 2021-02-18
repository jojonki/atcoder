import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def match(s1, s2):
    # print('match', s1, s2)
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        if c1 == '?' or c2 == '?':
            continue
        elif c1 == c2:
            continue
        else:
            return False
    return True


def calc(S, T):
    ins_pos = -1
    for i in range(len(S) - len(T) + 1, -1, -1):
        if match(S[i:i + len(T)], T):
            ins_pos = i
            break
    return ins_pos


def answer(ins_pos, S, T):
    S[ins_pos:ins_pos + len(T)] = T
    S = ''.join(S)
    S = S.replace('?', 'a')
    print(S)


def main():
    S = input()
    S2 = S.replace('?', 'a')
    S = list(S)
    S2 = list(S2)
    T = list(input())

    ins_pos = calc(S2, T)
    if ins_pos != -1:
        answer(ins_pos, S2, T)
    else:
        ins_pos = calc(S, T)
        if ins_pos == -1:
            print('UNRESTORABLE')
        else:
            answer(ins_pos, S, T)


main()
