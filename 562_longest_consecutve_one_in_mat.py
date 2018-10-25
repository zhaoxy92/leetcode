def longestLine(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """

    m, n = len(M),len(M[0])

    dp = [[[0, 0, 0]]*n for _ in range(m)]
    dp = [[[0 for _ in range(3)] for j in range(n)] for i in range(m)]

    best0, best1, best2 = 0, 0, 0

    if M[0][0] == 1:
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        dp[0][0][2] = 1
        best0, best1, best2 = 1, 1, 1

    for i in range(1,n):
        if M[0][i] == 1:
            dp[0][i][0] = dp[0][i-1][0] + 1
            dp[0][i][1] = 1
            dp[0][i][2] = 1
        if dp[0][i][0] > best0:
            best0 = dp[0][i][0]
        if dp[0][i][1] > best1:
            best1 = dp[0][i][1]
        if dp[0][i][2] > best2:
            best2 = dp[0][i][2]

    for i in range(1, m):
        if M[i][0] ==1:
            dp[i][0][0] = 1
            dp[i][0][1] = dp[i-1][0][1] + 1
            dp[i][0][2] = 1
        if dp[i][0][0] > best0:
            best0 = dp[i][0][0]
        if dp[i][0][1] > best1:
            best1 = dp[i][0][1]
        if dp[i][0][2] > best2:
            best2 = dp[i][0][2]

    for i in range(1,m):
        for j in range(1,n):
            if M[i][j]==1:
                dp[i][j][0] = dp[i][j - 1][0] + 1
                dp[i][j][1] = dp[i - 1][j][1] + 1
                dp[i][j][2] = dp[i - 1][j - 1][2] + 1
            else:
                dp[i][j][0] = 0
                dp[i][j][1] = 0
                dp[i][j][2] = 1

            if dp[i][j][0] > best0:
                best0 = dp[i][j][0]
            if dp[i][j][1] > best1:
                best1 = dp[i][j][1]
            if dp[i][j][2] > best2:
                best2 = dp[i][j][2]

    for line in dp:
        print(line)
    return max(best0, best1, best2)


# print(longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))

print(longestLine([[1,1,1,1],[0,1,1,0],[0,0,0,1]]))

# 1 1 1 1
# 0 1 1 0
# 0 0 0 1