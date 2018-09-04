import math
def kthGrammar(N, K):
    """
    :type N: int
    :type K: int
    :rtype: int
    """
    if N == 1: return 0

    if kthGrammar(N-1, math.ceil(K/2)) == 0:
        if K%2==0:
            return 1
        return 0
    else:
        if K % 2 == 0:
            return 0
        return 1

# print(kthGrammar(1,1))
# print(kthGrammar(2,1))
# print(kthGrammar(2,2))
print(kthGrammar(3,1))
# print(kthGrammar(4,5))