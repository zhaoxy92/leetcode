import string
def findSubstringInWraproundString(p):
    """
    :type p: str
    :rtype: int
    """

    if len(p) <= 1: return len(p)

    letters = string.ascii_lowercase
    letter2num = {letters[i]:i for i in range(len(letters))}
    cnt = {letters[i]:0 for i in range(len(letters))}
    cnt_max = {letters[i]:0 for i in range(len(letters))}

    cnt[p[0]] = 1
    cnt_max[p[0]] = 1

    for i in range(1, len(p)):
        if (letter2num[p[i]] - letter2num[p[i-1]] == 1) or (p[i]=='a' and p[i-1]=='z'):
            cnt[p[i]] = cnt[p[i-1]] + 1
        else:
            cnt[p[i]] = 1

        cnt_max[p[i]] = max(cnt_max[p[i]], cnt[p[i]])
    print(cnt)
    return sum(cnt_max.values())


print(findSubstringInWraproundString('cdefghefghijkl'))