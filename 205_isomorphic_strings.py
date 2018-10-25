def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if not len(s) == len(t): return False

    mapping = {}
    mapping_back = {}
    for i in range(len(s)):
        if s[i] in mapping:
            if not mapping[s[i]] == t[i]:
                return False
        else:
            if t[i] in mapping_back:
                return False
            mapping[s[i]] = t[i]
            mapping_back[t[i]] = s[i]

    return True

print(isIsomorphic(s = "egg", t = "add"))
print(isIsomorphic(s = "foo", t = "bar"))
print(isIsomorphic(s = "paper", t = "title"))
print(isIsomorphic(s = "ab", t = "aa"))