import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = input()
    ans = ''
    cur_c = S[0]
    ct = 1
    for i in range(1, len(S)):
        if S[i] == cur_c:
            ct += 1
        else:
            ans += f'{cur_c}{ct}'
            cur_c = S[i]
            ct = 1
    if ct != 0:
        ans += f'{cur_c}{ct}'
    print(ans)


main()
