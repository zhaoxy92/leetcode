def wordBreak(s, wordDict):

    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for k in range(i):
            if dp[k] and s[k:i] in wordDict:
                dp[i] = True

    return dp[-1]


print(wordBreak(s = "leetcode", wordDict = ["leet", "code"]))