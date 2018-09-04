def new21Game(self, N, K, W):
    """
    :type N: int
    :type K: int
    :type W: int
    :rtype: float
    """


    dp = [0] * (K+W-1)
    for i in range(K, len(dp)):
        if dp[i]>=K and dp[i]<=N:
            dp[i] = 1

    for i in range(len(dp)-1, -1, -1):
        