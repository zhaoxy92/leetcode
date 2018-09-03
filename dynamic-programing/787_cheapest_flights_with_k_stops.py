import math
def findCheapestPrice(n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """

    prices = {}
    for s, e, p in flights:
        prices[(s,e)] = p

    dp = [[math.inf for _ in range(n)] for _ in range(K+1)]
    for k in range(K+1):
        dp[k][dst] = 0

    for i in range(n):
        if (i,dst) in prices:
            dp[0][i] = prices[(i, dst)]

    for k in range(1, K+1):
        for i in range(n):
            cur = math.inf
            for g in range(n):
                t = 0
                if g == i:
                    t = dp[k - 1][g]
                elif (g,dst) in prices:
                    t = dp[k-1][g] + prices[(g, dst)]
                else:
                    t = math.inf
                if t < cur:
                    cur = t
            dp[k][i] = cur


    return dp[K][src]


# print(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1))
# print(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0))
print(findCheapestPrice(5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1))
# print(findCheapestPrice(3, [[0,1,2],[1,2,1],[2,0,10]], 1, 2, 1))