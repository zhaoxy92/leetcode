def findLength(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """

    dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    m = 0
    for i in range(1,(len(A)+1)):
        for j in range(1,(len(B)+1)):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0

            m = max(dp[i][j], m)

    return m

#
print(findLength([1,2,3,2,1], [3,2,1,4,7]))
print(findLength([0,0,0,0,0], [0,0,0,0,0]))
print(findLength([0,0,1], [1,0,0]))
