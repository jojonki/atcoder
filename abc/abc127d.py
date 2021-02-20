import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


# import heapq

from collections import defaultdict


def main():
    N, M = read_ints()
    # A = read_int_list()
    # A.sort()
    A = defaultdict(int)
    for a in read_int_list():
        A[a] += 1
    for _ in range(M):
        B, C = read_ints()
        A[C] += B
    # print(A)

    ans = 0
    cur_ct = 0
    sorted_A = sorted(A.items(), key=lambda x: -x[0])
    # print(sorted_A)
    for v, ct in sorted_A:
        if cur_ct + ct < N:
            ans += v * ct
            cur_ct += ct
        else:
            ans += v * (N - cur_ct)
            break
    print(ans)

    # TLE
    # for _ in range(M):
    #     B, C = read_ints()
    #     A += [C] * B
    # A.sort(reverse=True)
    # print(sum(A[:N]))

    # # TLE
    # heapq.heapify(A)
    # for _ in range(M):
    #     B, C = read_ints()
    #     for _ in range(B):
    #         v = heapq.heappop(A)
    #         heapq.heappush(A, max(v, C))
    # print(sum(A))


main()
