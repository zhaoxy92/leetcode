from collections import Counter
def findNumberOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    dp = [1 for _ in range(len(nums))]
    count = [1 for _ in range(len(nums))]
    for i in range(1, len(dp)):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j]+1 == dp[i]:
                    count[i] += count[j]


    max_len = max(dp)
    s = 0
    for i in range(len(dp)):
        if dp[i] == max_len:
            s += count[i]

    return s


# print(findNumberOfLIS([1,3,5,4,7]))
# print(findNumberOfLIS([2,2,2,2,2]))
print(findNumberOfLIS([1,2,4,3,5,4,7,2]))