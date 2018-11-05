def numMusicPlaylists(N, L, K):
    """
    :type N: int
    :type L: int
    :type K: int
    :rtype: int
    """

    mod = 10**9 + 7

    dp = [[0]*(L+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(1,L+1):
            dp[i][j] = dp[i-1][j-1]*(N-(i-1))
            dp[i][j] %= mod
            if i-K>0:
                dp[i][j] += dp[i][j-1] * (i-K)
                dp[i][j] %= mod

    return dp[-1][-1]


print(numMusicPlaylists( N = 3, L = 3, K = 1))
print(numMusicPlaylists(N = 2, L = 3, K = 0))
print(numMusicPlaylists(N = 2, L = 3, K = 1))