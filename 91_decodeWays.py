def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """

    if s.startswith('0'):
        return 0

    if len(s) <= 1:
        return len(s)


    dp = [0] * len(s)
    dp[0] = 1

    if s[1] == '0':
        if s[0] == '1' or s[0] == '2':
            dp[1] = 1
        else:
            return 0
    elif int(s[:2]) >= 1 and int(s[:2]) <=26:
        dp[1] = 2
    else:
        dp[1] = 1

    for i in range(2,len(s)):
        if s[i] == '0':
            if s[i - 1] == '2' or s[i - 1] == '1':
                dp[i] = dp[i - 2]
            else:
                return 0
        else:
            if s[i-1] == '0':
                dp[i] = dp[i-2]
            elif int(s[i-1:i+1]) >= 1 and int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]

    print(dp)
    return dp[-1]








# d(i) = d(i-1)
# d(i) = d(i-2) + 2
# print(numDecodings('10'))
# print(numDecodings('100'))
print(numDecodings('301'))

# print(numDecodings('12342346'))