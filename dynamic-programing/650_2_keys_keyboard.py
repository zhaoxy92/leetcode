def minSteps(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1: return 0
    elif n <=2 : return n

    dp = [0 for _ in range(n)]

    dp[1] = 2
    dp[2] = 3

    for i in range(3, n):
        for j in range(2,i):
            if (i+1)%j==0:
                dp[i] = j + dp[(i+1)//j-1]
                break
            dp[i] = i+1
    return dp[-1]


print(minSteps(247))
