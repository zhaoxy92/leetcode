def findLongestChain(pairs):
    """
    :type pairs: List[List[int]]
    :rtype: int
    """

    pairs = sorted(pairs, key=lambda x: x[1])

    dp = [1 for _ in range(len(pairs))]

    for i in range(len(dp)):
        p = i-1
        while p >= 0:
            if pairs[p][1] < pairs[i][0] and dp[p]+1 > dp[i]:
                dp[i] = dp[p] + 1
            p -= 1

    return max(dp)

print(findLongestChain([[1,2], [2,3], [3,4]]))