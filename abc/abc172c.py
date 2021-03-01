import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


# from collections import deque


def read_ints():
    return map(int, input().split())


def upperBound(nums, key):
    """numsの中でkeyより大きい要素のうちの一番左のインデックス"""
    ng, ok = -1, len(nums)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key < nums[mid]:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N, M, K = read_ints()
    A = read_int_list()
    B = read_int_list()

    SA = [0]
    SB = [0]
    for i in range(1, max(N + 1, M + 1)):
        if i - 1 < N:
            SA.append(SA[i - 1] + A[i - 1])
        if i - 1 < M:
            SB.append(SB[i - 1] + B[i - 1])
    # print(SA)
    # print(SB)

    ans = 0
    for i in range(N + 1):
        if SA[i] > K:
            break
        ok, ng = 0, len(SB)
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if SA[i] + SB[mid] <= K:
                ok = mid
            else:
                ng = mid
        ans = max(ans, i + ok)

        # for j in range(M + 1):
        #     if SA[i] + SB[j] <= K:
        #         # if i + j > ans:
        #         #     print(i, j, SA[i] + SB[j], ans, i + j)
        #         ans = max(ans, i + j)
        #     else:
        #         break
    print(ans)


main()
