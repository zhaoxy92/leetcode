def minFlipsMonoIncr(S):
    """
    :type S: str
    :rtype: int
    """

    dp = [[0, 0] for _ in range(len(S))]
    if S[0] == '0': dp[0][1] = 1
    if S[0] == '1': dp[0][0] = 1
    for i in range(1, len(S)):

        if S[i] == '0':
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + 1
        if S[i] == '1':
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = min(dp[i - 1][1], dp[i - 1][0])
    return min(dp[-1])