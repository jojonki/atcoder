import sys
from typing import DefaultDict
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def calc(vals):
    score = 0
    for i in range(1, 10):
        score += i * (10**vals.count(i))
    return score


def combi(n, k):
    if k < 0:
        return 0
    # nCk
    res = 1
    k = min(k, n - k)
    for i in range(k):
        res = res * (n - i)
        res = res / i + 1
    return res


def main():
    K = int(input())
    S = [int(v) for v in input()[:-1]]
    T = [int(v) for v in input()[:-1]]
    Counter = defaultdict(int)
    for c in S:
        Counter[c] += 1
    for c in T:
        Counter[c] += 1
    # print(Counter)

    win = 0
    total = (9 * K - 8)
    total = total * (total - 1)

    for i in range(1, 10):  # Takahachi
        if Counter[i] >= K:
            continue
        for j in range(1, 10):  # Aoki
            ok = False
            # if i == j:
            #     if Counter[i] - 2 > K:
            #         continue
            #     else:
            #         ok = True
            if ok or Counter[j] + 1 <= K:
                # print(S + [i], T + [j], calc(S + [i]) > calc(T + [j]))
                if calc(S + [i]) > calc(T + [j]):
                    # print(S + [i], T + [j], calc(S + [i]) > calc(T + [j]))
                    if i != j:
                        win += max(0, (K - Counter[i])) * max(
                            0, (K - Counter[j]))
                    else:
                        win += max(0, (K - Counter[i])) * max(
                            0, (K - Counter[j] - 1))

    # print(win, total)
    print(win / total)


main()
