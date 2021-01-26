def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict
from itertools import combinations

import math


def main():
    N = int(input())
    D = defaultdict(list)
    for _ in range(N):
        s = input()
        if s[0] in ['M', 'A', 'R', 'C', 'H']:
            D[s[0]].append(s)
    # print(D)
    ans = 0
    for combi in combinations(list(D.keys()), 3):
        # print(combi)
        # print([len(D[k]) for k in combi])
        ans += math.prod([len(D[k]) for k in combi])
    print(ans)


main()
