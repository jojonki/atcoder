def lower_bound(nums, key):
    """numsの中でkey以上の要素のうちの一番左のインデックス"""
    ng, ok = -1, len(nums)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key <= nums[mid]:
            ok = mid
        else:
            ng = mid
    return ok


def upper_bound(nums, key):
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
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    # print(A)
    # print(B)
    # print(C)

    ct = 0
    for b in B:
        # print('b=', b)
        a_ct = lower_bound(A, b)
        # print(f'lb', '=', lower_bound(A, b))
        c_ct = len(C) - upper_bound(C, b)
        # print('ub', '=', upper_bound(C, b))
        # print('b', a_ct, c_ct)
        ct += a_ct * c_ct

    print(ct)


main()
