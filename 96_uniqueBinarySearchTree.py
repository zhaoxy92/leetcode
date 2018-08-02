def numTrees(n):
    """
    :type n: int
    :rtype: int
    """

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1


    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]

    print(dp)
    return dp[-1]


print(numTrees(3))