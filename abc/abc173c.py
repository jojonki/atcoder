from itertools import combinations


def main2():
    ans = 0
    H, W, K = map(int, input().split())
    D = []
    for _ in range(H):
        tmp = []
        for c in input():
            tmp.append(c)
        D.append(tmp)
    # print(D)

    h_list = [h for h in range(H)]
    w_list = [w for w in range(W)]

    for n_h in range(H + 1):
        for n_w in range(W + 1):
            for rows in combinations(h_list, n_h):
                for cols in combinations(w_list, n_w):
                    ct = 0
                    # print(rows, cols)
                    for i in range(H):
                        if i in rows:
                            continue
                        for j in range(W):
                            if j in cols:
                                continue
                            if D[i][j] == '#':
                                ct += 1
                                if ct > K:
                                    break
                    if ct == K:
                        ans += 1

    print(ans)


def main():
    ans = 0
    H, W, K = map(int, input().split())
    D = []
    for _ in range(H):
        tmp = []
        for c in input():
            tmp.append(c)
        D.append(tmp)
    # print(D)
    for mask_r in range(1 << H):
        for mask_c in range(1 << W):
            # print(mask_r, mask_c)
            ct = 0
            for i in range(H):
                if mask_r >> i & 1 == 1:
                    continue
                for j in range(W):
                    if mask_c >> j & 1 == 1:
                        continue
                    if D[i][j] == '#':
                        ct += 1
                        if ct > K:
                            break
            if ct == K:
                ans += 1

    print(ans)


main()
# main2()
