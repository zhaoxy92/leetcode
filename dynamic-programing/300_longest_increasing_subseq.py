def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # dp[i] stores the max number of elements that are smaller than nums[i]

    if len(nums) == 1:
        return 1


    dp = [0] * len(nums)
    for i in range(1, len(nums)):
        dp[i] = 0
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
    return max(dp) + 1


print(lengthOfLIS([10,9,2,3,7,1,18,4,6,1,5,123,54,2,7]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))

print(lengthOfLIS([10,9,2,5,3,7,101,18]))


