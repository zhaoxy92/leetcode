def robFrom(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[-1]


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    return max(robFrom(nums[1:]),robFrom(nums[:-1]))

print(rob([3,1,3,4]))
print(rob([2,3,2]))