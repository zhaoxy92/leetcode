def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    for line in matrix:
        print(line)

    if len(matrix) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if matrix[i][0] == '1':
            dp[i][0] = 1
    for j in range(n):
        if matrix[0][j] == '1':
            dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = 0


    return max([item for row in dp for item in row]) ** 2


print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
# print(maximalSquare([["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]))