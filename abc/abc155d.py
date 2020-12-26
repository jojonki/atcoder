N, K = map(int, input().split())
A = list(map(int, input().split()))

def smallestDistancePair(nums, k):
    def possible(guess):
        #Is there k or more pairs with distance <= guess?
        return sum(prefix[min(x + guess, W)] - prefix[x] + multiplicity[i]
                    for i, x in enumerate(nums)) >= k

    nums.sort()
    W = nums[-1]

    #multiplicity[i] = number of nums[j] == nums[i] (j < i)
    multiplicity = [0] * len(nums)
    for i, x in enumerate(nums):
        if i and x == nums[i-1]:
            multiplicity[i] = 1 + multiplicity[i - 1]

    #prefix[v] = number of values <= v
    prefix = [0] * (W + 1)
    left = 0
    for i in range(len(prefix)):
        while left < len(nums) and nums[left] == i:
            left += 1
        prefix[i] = left

    lo = 0
    hi = nums[-1] - nums[0]
    while lo < hi:
        mi = (lo + hi) / 2
        if possible(mi):
            hi = mi
        else:
            lo = mi + 1

    return lo

print(smallestDistancePair(A, K))

# A = sorted(A)
# posIdx = None
# for i, a in enumerate(A):
#     if a >= 0:
#         posIdx = i
#         break
# n_neg = posIdx
# n_pos = len(A) - posIdx

# if K <= n_neg * n_pos: # neg
#     negs = []
#     for n_v in A[:posIdx]:
#         for p_v in A[posIdx:]:
#             negs.append(n_v*p_v)
#     negs = sorted(negs)
#     print(negs[K-1])
# else: # pos
#     poss = A[posIdx:]
#     combi = []
#     for i in range(len(poss)-1):
#         for j in range(i+1, len(poss)):
#             combi.append(poss[i]*poss[j])
#     for i in range(n_neg-1):
#         for j in range(i+1, n_neg):
#             combi.append(A[i]*A[j])
#     combi = sorted(combi)
#     print(combi[K-1 - n_neg*n_pos])