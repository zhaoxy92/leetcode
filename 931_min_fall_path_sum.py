def minFallingPathSum(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """

    m, n = len(A), len(A[0])
    pre = A[0]
    dp = [0]*n
    for i in range(1, m):
        for j in range(n):
            if j-1>=0 and j+1<=n-1:
                dp[j] = A[i][j] + min(pre[j - 1], pre[j], pre[j + 1])
            elif j-1>=0:
                dp[j] = A[i][j] + min(pre[j - 1], pre[j])
            elif j+1<=n-1:
                dp[j] = A[i][j] + min(pre[j], pre[j + 1])
            else:
                dp[j] = A[i][j] + pre[j]


        pre = dp
        dp = [0]*n

    return min(pre)

print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))