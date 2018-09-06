def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) <= 1: return len(s)

    i = 0
    j = 1
    best = 1
    record = {}
    record[s[0]] = 1
    while i<len(s) and j<len(s):
        if not s[j] in record:
            record[s[j]] = 1
            j += 1
            best = max(best, j-i)
        else:
            record.pop(s[i])
            i += 1


    return best

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbbbb'))
print(lengthOfLongestSubstring('pwwk'))

