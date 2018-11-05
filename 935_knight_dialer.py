def knightDialer(N):
    """
    :type N: int
    :rtype: int
    """

    dp = [[0]*10 for _ in range(N)]
    dp[0] = [1]*10

    for i in range(1, N):
        dp[i][0] = (dp[i - 1][4] + dp[i - 1][6])%1000000007
        dp[i][1] = (dp[i - 1][6] + dp[i - 1][8])%1000000007
        dp[i][2] = (dp[i - 1][7] + dp[i - 1][9])%1000000007
        dp[i][3] = (dp[i - 1][4] + dp[i - 1][8])%1000000007
        dp[i][4] = (dp[i - 1][0] + dp[i - 1][3] + dp[i - 1][9])%1000000007
        dp[i][6] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][7])%1000000007
        dp[i][7] = (dp[i - 1][2] + dp[i - 1][6])%1000000007
        dp[i][8] = (dp[i - 1][1] + dp[i - 1][3])%1000000007
        dp[i][9] = (dp[i - 1][2] + dp[i - 1][4])%1000000007


    return sum(dp[-1])%1000000007
print(knightDialer(1))
print(knightDialer(2))
print(knightDialer(3))
print(knightDialer(161))