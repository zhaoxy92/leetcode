
# "(1+(4+5+2)-3)+(6+8)"

def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    stack = []
    res = 0
    sign = 1
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            cur = c
            while i+1 < len(s) and s[i+1].isdigit():
                cur += s[i+1]
                i += 1
            cur = int(cur)
            res += sign * cur
        elif c == '-':sign = -1
        elif c == '+': sign = 1
        elif c == '(':
            stack.append(res)
            res = 0
            stack.append(sign)
            sign = 1
        elif c == ')':
            res = stack.pop()*res + stack.pop()
            sign = 1

        i += 1


    return res

print(calculate("(2147483647+1)"))