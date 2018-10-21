def dailyTemperatures( T):
    """
    :type T: List[int]
    :rtype: List[int]
    """

    res = [0] * len(T)
    min_idx = {}
    for i in range(len(T)-1,-1, -1):
        min_idx[T[i]] = i
        z = 0
        for t in range(T[i]+1, 101):
            if t in min_idx and (z == 0 or min_idx[t]<z):
                z = min_idx[t]


        res[i] = z-i if z>0 else 0

    return res

print(dailyTemperatures( [73, 74, 75, 71, 69, 72, 76, 73]))