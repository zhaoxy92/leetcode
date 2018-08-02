def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int

    index status: 0: buy, 1:sell, 2: cooldown

    """

    s0 = [0] * len(prices) # buy
    s1 = [0] * len(prices) # sell
    s2 = [0] * len(prices) # cooldown

    s0[0] = -prices[0]
    s1[0] = -999999999
    s2[0] = 0


    for i in range(1, len(prices)):

        s0[i] = max(s2[i-1]-prices[i], s0[i-1])
        s1[i] = s0[i-1] + prices[i]
        s2[i] = max(s1[i-1], s2[i-1])

    return max(s1[-1], s2[-1])


print(maxProfit([1,2,3,0,2]))

