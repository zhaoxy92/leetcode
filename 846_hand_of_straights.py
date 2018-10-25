import collections
def isNStraightHand(hand, W):
    """
    :type hand: List[int]
    :type W: int
    :rtype: bool
    """

    count = collections.Counter(hand)
    while count:
        m = min(count)
        for k in range(m, m + W):
            v = count[k]
            if not v: return False
            if v == 1:
                del count[k]
            else:
                count[k] = v - 1

    return True


print(isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], W = 3))
print(isNStraightHand(hand = [1,2,3,4,5], W = 4))