def integerBreak(n):
    """
    :type n: int
    :rtype: int
    """
    # find pattern, also substract 3 first
    if n==2: return 1
    if n==3: return 2

    total = 1
    left = n
    while not left == 2 and not left == 4:
        total *= 3
        left -= 3

    return total * left

print(integerBreak(10))