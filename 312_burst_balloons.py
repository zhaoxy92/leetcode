

def maxCoins(self, iNums):
    nums = [1] + [i for i in iNums if i > 0] + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for k in range(2, n):
        for left in range(0, n - k):
            right = left + k
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right],
                                      nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]


def maxCoins(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for j in range(n + 2)] for i in range(n + 2)]

    def DP(i, j):
        if dp[i][j] > 0: return dp[i][j]
        for x in range(i, j + 1):
            dp[i][j] = max(dp[i][j], DP(i, x - 1) + nums[i - 1] * nums[x] * nums[j + 1] + DP(x + 1, j))
        return dp[i][j]

    return DP(1, n)