def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """

    if n==0: return False

    while n%3==0:
        n = n//3

    if n==1:
        return True
    return False


print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(9))
print(isPowerOfThree(45))