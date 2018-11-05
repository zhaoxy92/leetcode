def sortArrayByParityII(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    if not A: return A

    even, odd = [],[]
    for a in A:
        if a%2==0:
            even.append(a)
        else:
            odd.append(a)
    ans = []
    for i in range(len(A)):

        if even:ans.append(even.pop())
        if odd: ans.append(odd.pop())
    return ans