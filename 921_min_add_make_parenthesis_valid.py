def minAddToMakeValid(S):
    """
    :type S: str
    :rtype: int
    """

    stack = []
    for s in S:
        if stack and s==')' and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(s)
    return len(stack)

print(minAddToMakeValid("())"))
print(minAddToMakeValid("((("))
print(minAddToMakeValid("()"))
print(minAddToMakeValid("()))(("))

