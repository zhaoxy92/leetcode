# def mincostToHireWorkers(quality, wage, K):
#     """
#     :type quality: List[int]
#     :type wage: List[int]
#     :type K: int
#     :rtype: float
#     """
#     ans = -1
#     N = len(quality)
#     for prime in range(N):
#
#         factor = wage[prime] / quality[prime]
#         prices = [wage[prime]]
#
#         for i in range(N):
#             if not i==prime:
#                 price = quality[i] * factor
#                 if price >= wage[i]:
#                     prices.append(price)
#
#         if len(prices) < K: continue
#
#         prices.sort()
#         if ans == -1:
#             ans = sum(prices[:K])
#         else:
#             ans = min(ans, sum(prices[:K]))
#
#     return ans

import heapq

def mincostToHireWorkers(quality, wage, K):
    from fractions import Fraction
    workers = sorted((Fraction(w, q), q, w)
                     for q, w in zip(quality, wage))

    ans = float('inf')
    pool = []
    sumq = 0
    for ratio, q, w in workers:
        heapq.heappush(pool, -q)  # it's a minheap. we want to use maxheap, so push -q
        sumq += q

        if len(pool) > K:
            sumq += heapq.heappop(pool)

        if len(pool) == K:
            ans = min(ans, ratio * sumq)

    return float(ans)

print(mincostToHireWorkers([10,20,5], [70,50,30], 2))
print(mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))