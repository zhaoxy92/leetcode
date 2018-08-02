def numSquares(n):
    """
    :type n: int
    :rtype: int
    """

    nums = []
    c = 0
    while c ** 2 <= n:
        nums.append(c ** 2)
        c += 1

    if n in nums:
        return 1

    dp = [1] * n

    for i in range(1, n):
        if i+1 in nums:
            continue
        else:
            m = i+1
            j = 1
            while i - j*j >=0:
                m = min(m, dp[i-j*j]+1)
                j += 1
            dp[i] = m

    print(dp)
    return dp[-1]

print(numSquares(12))
print(numSquares(382))

