def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """

    if len(cost)<=2: return 0

    dp = [0 for _ in range(len(cost))]

    for i in range(2, len(cost)):
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return min(cost[-1]+dp[-1], cost[-2]+dp[-2])


print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

