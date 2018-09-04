

def largestSumOfAverages(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: float
    """

    N = len(A)
    dp = [avg(i, N, A) for i in range(N)]
    for k in range(K-1):
        for i in range(N):
            for j in range(i+1, N):

                dp[i] = max(dp[i], avg(i, j, A) + dp[j])

    return dp[0]

def avg(i, j, A):
    return (sum(A[:j])-sum(A[:i]))/(j-i)

print(largestSumOfAverages([1,2,3,4,5,6,7], 4))