# けんちょんさんのめぐるん式二部探索解説
# https://qiita.com/drken/items/97e37dd6143e33a64c8c

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

def printResult(nums, key):
    idx = lowerBound(nums, key)
    if idx < len(nums):
        print('LB: key={}, nums[{}]={}'.format(key, idx, nums[idx]))
    else:
        print('LB: key={}, nums[{}]= out-of-range'.format(key, idx))

    idx = upperBound(nums, key)
    if idx < len(nums):
        print('UB: key={}, nums[{}]={}'.format(key, idx, nums[idx]))
    else:
        print('UB: key={}, nums[{}]= out-of-range'.format(key, idx))

def main():
    nums1 = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]
    printResult(nums1, -1)
    printResult(nums1, 50)
    printResult(nums1, 51)
    printResult(nums1, 999)

    # LB: key=-1, nums[0]=1
    # UB: key=-1, nums[0]=1
    # LB: key=50, nums[3]=51
    # UB: key=50, nums[3]=51
    # LB: key=51, nums[3]=51
    # UB: key=51, nums[6]=243
    # LB: key=999, nums[10]= out-of-range
    # UB: key=999, nums[10]= out-of-range

if __name__ == '__main__':
    main()