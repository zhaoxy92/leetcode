def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1

    dp = [1] * n
    i, j, k = 0, 0, 0

    for ix in range(1, n):
        dp[ix] = min(dp[i]*2, dp[j]*3, dp[k]*5)

        if dp[i]*2 == dp[ix]: i += 1
        if dp[j]*3 == dp[ix]: j += 1
        if dp[k]*5 == dp[ix]: k += 1

    print(dp)
    return dp[-1]


print(nthUglyNumber(10))