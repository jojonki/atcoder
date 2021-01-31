import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from itertools import product


def main():
    N, M = read_ints()
    Cond = []
    for _ in range(M):
        A, B = read_ints()
        A -= 1
        B -= 1
        if A > B:
            A, B = B, A
        # key = f'{A}-{B}'
        Cond.append((A, B))

    K = int(input())
    P = []
    for _ in range(K):
        C, D = read_ints()
        C -= 1
        D -= 1
        P.append((C, D))

    ans = 0
    for balls in product(*P):
        # print(balls)
        balls = set(balls)
        ct = 0
        for A, B in Cond:
            if A in balls and B in balls:
                ct += 1
        ans = max(ans, ct)
    print(ans)

    # at contest
    # seed = [k for k in range(K)]
    # for k in range(K):  # k人はCを採用
    #     pairs = combinations(seed, k)
    #     for p in pairs:
    #         balls = [0] * (N + 1)
    #         for k2 in range(K):
    #             if k2 in p:
    #                 v = P[k2][0]
    #             else:
    #                 v = P[k2][1]
    #             balls[v] += 1

    #         satisfy = 0
    #         for A, B in Cond:
    #             if balls[A] != 0 and balls[B] != 0:
    #                 satisfy += 1
    #         ans = max(ans, satisfy)


#
# print(ans)

main()
