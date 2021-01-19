from collections import defaultdict


def main():
    N, M = map(int, input().split())
    res = {'AC': set(), 'WA': {i: 0 for i in range(N)}}
    for _ in range(M):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            res[s].add(p)
        else:
            if p not in res['AC']:
                res['WA'][p] += 1

    n_wa = 0
    for p, wa_ct in res['WA'].items():
        if p in res['AC']:
            n_wa += wa_ct

    print(len(res['AC']), n_wa)


main()
