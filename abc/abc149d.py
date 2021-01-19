def kachi(aite):
    if aite == 'r':
        return 'p'
    elif aite == 's':
        return 'r'
    else:  # p
        return 's'


def aiko(aite):
    return aite


def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    score = {'r': R, 's': S, 'p': P}
    T = input()
    ans = 0

    for id_in_group in range(K):
        # print('id_in_group', id_in_group)
        prev_te = ''
        for group_id in range(N // K + 2):
            i = K * group_id + id_in_group
            if i >= N:
                break

            aite = T[i]
            kachi_te = kachi(aite)
            # print('Group', group_id, 'i=', i, aite, prev_te)
            if kachi_te != prev_te:
                ans += score[kachi_te]
                prev_te = kachi_te
            else:
                next_kachi_te = ''
                next_i = i + K
                if next_i < N:
                    next_aite = T[next_i]
                    next_kachi_te = kachi(next_aite)
                prev_te = ['r', 's', 'p']
                prev_te.remove(kachi_te)
                if next_kachi_te in prev_te:
                    prev_te.remove(next_kachi_te)
                # print(aite, prev_te)
                prev_te = prev_te[0]
                # print(prev_te)
    #         print('te', prev_te)
    # print('te', prev_te)
    print(ans)


main()
