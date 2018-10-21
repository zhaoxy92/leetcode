def anagramMappings(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    pos = {}
    for i in range(len(B)):
        if B[i] in pos:
            pos[B[i]].append(i)
        else:
            pos[B[i]] = [i]
    P = []
    for i in range(len(A)):
        idx = pos[A[i]].pop()
        P.append(idx)

    return P