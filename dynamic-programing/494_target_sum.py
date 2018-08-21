import collections
def findTargetSumWays(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """


    dp = [collections.Counter() for _ in range(len(nums)+1)]
    dp[0][0] = 1

    for i in range(len(nums)):
        for s, cnt in dp[i].items():
            dp[i+1][s+nums[i]] += cnt
            dp[i+1][s-nums[i]] += cnt


    return dp[-1][S]


print(findTargetSumWays([1,1,1,1,1],3))
