def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    dp = [0] + [-1] * amount
    for money in range(1, len(dp)):
        temp = []
        for c in coins:
            if money-c >=0 and dp[money-c]>=0:
                temp.append(dp[money-c])
        if not temp == []:
            dp[money] = min(temp) + 1

    print(dp)
    return dp[-1]
print(coinChange([1,5,2],11 ))
print(coinChange([186,419,83,408], 83))