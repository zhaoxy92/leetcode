def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']

    stack = []
    for l in s:
        if l in vowels:
            stack.append(l)
    new_s = ''
    for i in range(len(s)):
        if s[i] in vowels:
            new_s += stack.pop()
        else:
            new_s += s[i]
    return new_s

print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
