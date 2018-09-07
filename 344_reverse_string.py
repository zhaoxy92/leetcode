def reverseString(self, s):
    """
    :type s: str
    :rtype: str
    """



    return s[::-1]


def reverseString2(s):

    return s[-1] + reverse(s[:-1])

def reverse(s):
    if len(s)<=1:
        return s
    return s[-1]+reverse(s[:-1])

print(reverseString2('abcde'))