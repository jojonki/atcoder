def main():
    D, G = map(int, input().split())

    score_data = []
    for i in range(D):
        q = []
        p, c = map(int, input().split())
        score_data.append((p, c))

    min_ct = float('inf')
    for bit in range(1 << D):
        ct = 0
        score = 0

        # 全完
        for j in range(D):
            if (1 << j) & bit:
                p, c = score_data[j]
                score += 100 * (j + 1) * p + c
                ct += p

        if score >= G:
            min_ct = min(min_ct, ct)
            continue
        else:
            # 他の問題を高い順に解く
            for k in range(D - 1, -1, -1):
                if (1 << k) & bit: continue
                p, _c = score_data[k]
                for _ in range(p):
                    score += 100 * (k + 1)
                    ct += 1
                    if score >= G:
                        min_ct = min(min_ct, ct)
                        break
    print(min_ct)


main()
