import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def f2(col):
    l, r = -1, -1
    # print(col)
    for i, v in enumerate(col):
        if v == '#':
            if l == -1:
                l = i
            elif col[i + 1] == '.':
                r = i
                break
    if r == -1:
        r = l
    # print(l, r)
    return l, r


def f(col):
    res = []
    for i, v in enumerate(col):
        if v == '#':
            res.append(i)
    return res


def main():
    H, W = read_ints()
    T = []
    ans = 0
    for _ in range(H):
        v = list(input())
        # if '#' in v:
        #     ans += 4
        T.append(v)

    # for t in T:
    #     print(t)

    for r in range(H - 1):
        for c in range(W - 1):
            lu = T[r][c]
            ru = T[r][c + 1]
            lb = T[r + 1][c]
            rb = T[r + 1][c + 1]
            res = [lu, ru, lb, rb]
            kuro_ct, shiro_ct = 0, 0
            for v in res:
                if v == '#':
                    kuro_ct += 1
                else:
                    shiro_ct += 1
            if kuro_ct == 3 or shiro_ct == 3:
                ans += 1

    print(ans)


main()
