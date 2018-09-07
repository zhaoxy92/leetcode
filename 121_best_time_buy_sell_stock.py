def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    minprice = -1
    bestprofit = -1

    for i in range(len(prices)):

        if prices[i] < minprice or minprice==-1:
            minprice = prices[i]
        elif prices[i] - minprice > bestprofit:
            bestprofit = prices[i] - minprice


    return bestprofit

