# dp = {}

def find_lowest_price(price, special, needs):

    # if tuple(needs) in dp:
    #     return dp[tuple(needs)]

    cost = 0
    for i, need in enumerate(needs):
        cost += need * price[i]

    for offer in special:

        for i, need in enumerate(needs):
            if need < offer[i]:
                break
        else:
            new_needs = [need-offer[i] for i, need in enumerate(needs)]
            cost = min(cost, offer[-1] + find_lowest_price(price, special, new_needs))

    # dp[tuple(needs)] = cost
    return cost

def shoppingOffers(price, special, needs):
    """
    :type price: List[int]
    :type special: List[List[int]]
    :type needs: List[int]
    :rtype: int
    """
    return find_lowest_price(price, special, needs)


print(shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))
print(shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))