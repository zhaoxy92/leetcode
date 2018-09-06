def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    if len(s) == 0: return True
    if len(s) % 2 == 1: return False

    left = ['(', '[', '{']
    right = [')', ']', '}']
    stack = []
    for p in s:
        if p in left:
            stack.append(p)
        else:
            if len(stack) > 0:
                l = stack.pop()
                if not right.index(p) == left.index(l):
                    return False
            else:
                return False

    if len(stack) > 0:
        return False
    return True

print(isValid("()"))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('([)]'))
print(isValid('{[]}'))
print(isValid('){'))
