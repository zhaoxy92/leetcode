#dp[i][j] = max(sum[i][j]-dp[i+1][j], sum[i][j]-dp[i][j-1])

def PredictTheWinner(nums):

    if len(nums) == 1:
        return True

    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][i] = nums[i]

    for step in range(1,len(nums)):
        for i in range(len(nums)-step):
            j = i + step

            dp[i][j] = max([sum(nums[i:j+1])-dp[i+1][j], sum(nums[i:j+1])-dp[i][j-1]])

    return dp[0][len(nums)-1] >= sum(nums)/2


print(PredictTheWinner([1,1]))