def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """

    # dp[i][j]: the longest length in substring[i,j]

    dp = [[0]*len(s) for _ in range(len(s))]
    for i in range(len(s)-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, len(s)):

            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])




    return dp[0][-1]


print(longestPalindromeSubseq('bbbab'))
print(longestPalindromeSubseq('cbbd'))