from itertools import permutations


def main():
    M = {}
    C = input()
    for c in C:
        c = int(c)
        if c not in M:
            M[c] = 1
        else:
            M[c] = min(3, M[c] + 1)

    # print(M)
    S = []
    for key, ct in M.items():
        S += [key] * ct
    # print(S)

    keta = min(len(S), 3)
    for ds in permutations(S, keta):
        # print(d1, d2, d3)
        v = sum([10**(keta - i - 1) * d for i, d in enumerate(ds)])
        # print('keta', keta, 'v=', v, ds)

        # if (100 * d1 + 10 * d2 + d3) % 8 == 0:
        if v % 8 == 0:
            print('Yes')
            return
    print('No')


main()
