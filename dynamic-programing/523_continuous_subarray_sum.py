def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    if len(nums) <2:
        return False
    if k ==0:
        return True if set(nums) == {0} else False

    record = [nums[0]]
    dp = [nums[0]] * len(nums)


    for i in range(1, len(nums)):
        dp[i] = dp[i-1] + nums[i]

        if dp[i] % k in record:
            return True

        record.append(dp[i]%k)

    print(record)
    if dp[-1]%k in record:
        return True

    return False

print(checkSubarraySum([23, 2, 4, 6, 7], 6))
print(checkSubarraySum([23,2,6,4,7], 0))
print(checkSubarraySum([0,0],0))
print(checkSubarraySum([1,1],2))
print(checkSubarraySum([1,2,3],4))