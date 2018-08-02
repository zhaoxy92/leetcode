def combinationSum2(nums, target):

    if target == 0:
        return 1

    res = 0
    for i in range(len(nums)):

        if target >= nums[i]:
            res += combinationSum2(nums, target-nums[i])
    return res

def combinationSum(nums, target):
    comb = [-1] * (target+1)
    comb[0] = 1

    for i in range(1, target+1):
        for j in range(len(nums)):
            if i >= nums[j]:
                comb[i] += comb[i-comb[j]]
    return comb[target]


