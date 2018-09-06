def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    best = ''
    for i in range(len(s)):
        temp = get_palindrome(s, i, i)
        if len(temp)>len(best):
            best = temp

    for i in range(len(s)-1):
        temp = get_palindrome(s, i, i+1)
        if len(temp)>len(best):
            best = temp
    return best


def get_palindrome(s, l, r):
    tmp = ''
    while l>=0 and r<=len(s)-1 and s[l]==s[r]:
        l -= 1
        r += 1
    return s[l+1:r]



print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))

