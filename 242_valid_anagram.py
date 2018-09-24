def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(s): return False

    counter = {}
    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    for char in t:
        if not char in counter:
            return False
        counter[char] -= 1

    return all(v==0 for v in counter.values())


print(isAnagram('anagram', 'nagaram'))