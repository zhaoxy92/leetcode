import string
def reverseOnlyLetters(S):
    """
    :type S: str
    :rtype: str
    """
    letters = string.ascii_letters

    s = ''
    skip = []
    stack = []
    for i in range(len(S)):
        if S[i] in letters:
            stack.append(S[i])
        else:
            skip.append(i)

    for i in range(len(S)):
        if i in skip:
            s += S[i]
        else:
            s += stack.pop()

    return s




print(reverseOnlyLetters("ab-cd"))
print(reverseOnlyLetters("a-bC-dEf-ghIj"))
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))