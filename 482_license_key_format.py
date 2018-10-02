def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """

    key_str = ''.join(S.split('-'))
    stack = []
    idx = len(key_str)-1
    k = 0
    while idx>=0:
        if k<K:
            stack.append(key_str[idx].upper())
            k += 1
        else:
            stack.append('-')
            stack.append(key_str[idx].upper())
            k = 1
        idx -=1

    ans = ''
    while stack:
        ans += stack.pop()

    return ans

print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(licenseKeyFormatting("2-5g-3-J",2))