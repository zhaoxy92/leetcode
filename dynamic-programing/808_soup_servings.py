record = {}
def soupServings(N):
    """
    :type N: int
    :rtype: float
    """

    return AEmptyFirst(N, N)

def AEmptyFirst(a,b):

    if a <= 0 and b<=0: return 0.5
    elif a<=0: return 1
    elif b<=0: return 0

    if (a,b) in record:
        return record[(a,b)]

    t = 0.25 * (AEmptyFirst(a-100, b) + AEmptyFirst(a-75, b-25) + AEmptyFirst(a-50, b-50) + AEmptyFirst(a-25, b-75))
    record[(a,b)] = t
    return t

print(soupServings(50))
