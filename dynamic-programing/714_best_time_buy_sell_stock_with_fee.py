def maxProfit(prices, fee):
    """
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """

    profit_if_hold = [0] * len(prices)
    profit_if_sell = [0] * len(prices)

    profit_if_hold[0] = -prices[0]

    for i in range(1, len(prices)):

        profit_if_hold[i] = max(profit_if_hold[i-1], profit_if_sell[i-1] - prices[i])
        profit_if_sell[i] = max(profit_if_sell[i-1], profit_if_hold[i-1] + prices[i] - fee)


    return profit_if_sell[-1]


print(maxProfit([1,3,7,5,10,3], 3))