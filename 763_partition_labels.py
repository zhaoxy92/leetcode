def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    """
    last = {c:i for i, c in enumerate(S)}
    start,j = 0,0
    ans = []
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i==j:
            ans.append(j-start+1)
            start = i+1
            j = 0


    return ans


print(partitionLabels('ababcbacadefegdehijhklij'))


