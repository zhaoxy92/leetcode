def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """

    # current row is the sum of last row and a transition to the right of last row
    k = rowIndex+1
    res = [1]*k

    if k<=2: return res

    res = [1,1]
    for i in range(3,k+1):
        res = [0] + res

        for j in range(len(res)-1):
            res[j] = res[j] + res[j+1]


    print(res)


getRow(4)