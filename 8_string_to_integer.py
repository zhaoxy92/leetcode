def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """

    num = 0
    sign = 1
    started = 0
    for c in str:

        if ord(c) > 47 and ord(c) < 58:
            num = 10 * num + int(c)
            started = 1
        elif (c) == ' ' and started == 0:
            continue
        elif c == "-" and started == 0:
            started = 1
            sign = -1
            continue
        elif c == "+" and started == 0:
            sign = 1
            started = 1
            continue
        else:
            break

    num = num * sign

    if num < -2 ** 31:
        return (-2 ** 31)
    if num > 2 ** 31 - 1:
        return (2 ** 31 - 1)

    return num

print(myAtoi("42"))
print(myAtoi("   -42"))
