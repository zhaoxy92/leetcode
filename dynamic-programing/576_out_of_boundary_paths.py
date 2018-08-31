def findPaths(m, n, N, i, j):
    """
    :type m: int
    :type n: int
    :type N: int
    :type i: int
    :type j: int
    :rtype: int
    """

    if N == 0: return 0

    dp = [[[0 for ii in range(n)] for jj in range(m)] for kk in range(N+1)]


    for Ni in range(N):
        for mi in range(m):
            for ni in range(n):

                d1 = 1 if mi == 0 else dp[Ni-1][mi - 1][ni]
                d2 = 1 if mi == m - 1 else dp[Ni-1][mi + 1][ni]
                d3 = 1 if ni == 0 else dp[Ni-1][mi][ni - 1]
                d4 = 1 if ni == n - 1 else dp[Ni-1][mi][ni + 1]

                dp[Ni][mi][ni] = d1 + d2 + d3 + d4



    return dp[N-1][i][j] % 1000000007


print(findPaths(2,2,2,0,0))
print(findPaths(3,3,1,2,2))