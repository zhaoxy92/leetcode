def twoSum(nums, target):

    record = {}
    for i in range(len(nums)):
        if (target - nums[i]) in record:
            return [i, record[target-nums[i]]]
        record[nums[i]] = i

    return []

print(twoSum([2,7,11,15], 9))