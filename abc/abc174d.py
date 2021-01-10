def lowerBound(nums, key):
    """numsの中でkey以上の要素のうちの一番左のインデックス"""
    ng, ok = -1, len(nums)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key <= nums[mid]:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N = int(input())
    C = input()
    res = 0
    l, r = 0, N - 1
    while l < r:
        while l < N and C[l] == 'R':
            l += 1
        while r >= 0 and C[r] == 'W':
            r -= 1
        if l >= r:
            break
        res += 1
        l += 1
        r -= 1
        # print(l, r)
    print(res)


main()
