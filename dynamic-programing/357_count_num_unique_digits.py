def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    # 3: 8
    #   4: 7
    # 5 6
    # 9 2
    # 10 1

    if n == 1: return 10
    if n == 2: return 10 + 9*9
    if n >= 11: return 0

    available = 8
    total = 10 + 9*9
    unique = 81
    for i in range(3, n+1):
        unique = unique * available
        total += unique
        available -= 1

    return total


print(countNumbersWithUniqueDigits(2))
