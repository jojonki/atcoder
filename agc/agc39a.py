import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main2():
    S = input()
    K = int(input())

    dup_ct = 0
    streak_c = ''
    streak_ct = 0
    flag = False
    if K > 1:
        S += S[0]
    for i, c in enumerate(S):
        if c != streak_c:
            streak_c = c
            streak_ct = 1
        else:
            streak_ct += 1
            if streak_ct == 2:
                dup_ct += 1
                streak_c = ''
                streak_ct = 0
                if i == len(S) - 1:
                    flag = True
    ans = dup_ct * K
    if flag and K > 1:
        ans -= 1
    print(ans)


def calc_dup_ct(S):
    streak_c = ''
    streak_ct = 0
    dup_ct = 0
    for c in S:
        if c == streak_c:
            streak_ct += 1
            if streak_ct == 2:
                dup_ct += 1
                streak_ct = 0
                streak_c = ''
        else:
            streak_c = c
            streak_ct = 1
    return dup_ct


def main():
    S = input()
    K = int(input())

    ans = 0
    if S[0] != S[-1] or K == 1:
        ans = calc_dup_ct(S) * K
    else:
        if len(set(S)) == 1:  # same values
            ans = (len(S) * K) // 2
        else:
            head_ct, tail_ct = 1, 1
            for i in range(1, len(S)):
                if S[i] == S[0]:
                    head_ct += 1
                else:
                    break
            for i in range(1, len(S)):
                if S[len(S) - 1 - i] == S[-1]:
                    tail_ct += 1
                else:
                    break
            ans = calc_dup_ct(S[head_ct:len(S) - tail_ct]) * K
            ans += head_ct // 2 + tail_ct // 2 + (
                (head_ct + tail_ct) // 2) * (K - 1)

    print(ans)


main()
