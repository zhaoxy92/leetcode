def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    if len(nums) < 3: return []
    nums = sorted(nums)
    res = []

    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        j = i + 1
        k = len(nums)-1

        target = -nums[i]

        while j<k:
            if nums[j] + nums[k] == target:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j<k and nums[j] == nums[j-1]: j += 1
                while j<k and nums[k] == nums[k+1]: k -= 1

            elif nums[j] + nums[k] > target:
                k-= 1
            else:
                j += 1

    return res

print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 0, 0,0]))