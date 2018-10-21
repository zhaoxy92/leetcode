def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2: return len(nums)
    
    nums.sort()
    dp = {n:1 for n in nums}
    best = 1
    for n in nums:
        if n-1 in dp:
            dp[n] = dp[n-1] + 1
            if dp[n] > best:
                best = dp[n]

    return best


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([1,0,1]))
print(longestConsecutive([1,2,0,1]))