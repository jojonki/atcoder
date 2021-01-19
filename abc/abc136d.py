def main():
    S = input()
    N = len(S)
    ans = []
    left, right = 0, 1
    while right < N:
        L_ct, R_ct = 0, 0
        while S[left] == 'R':
            R_ct += 1
            left += 1
        right = left
        while S[right] == 'L':
            L_ct += 1
            right += 1
            if right >= N:
                break

        # print(R_ct, L_ct)

        seq = [0] * (R_ct - 1)

        LR_ct = R_ct + L_ct
        if LR_ct % 2 == 0:
            r_v = LR_ct // 2
        elif R_ct % 2 == 1:
            r_v = LR_ct // 2 + 1
        else:
            r_v = LR_ct // 2

        seq.append(r_v)
        seq.append(LR_ct - seq[-1])

        seq += [0] * (L_ct - 1)
        ans += seq

        left = right

    ans = ' '.join(str(v) for v in ans)
    print(ans)
    # label = input()[1:]
    # print(ans, '--', label)
    # assert ans == label


main()
