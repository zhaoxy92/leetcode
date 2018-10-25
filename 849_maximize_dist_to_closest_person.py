def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    n = len(seats)
    left = [n] * n
    right = [n] * n

    for i in range(n):
        if seats[i]==1:
            left[i] = 0
        else:
            if i > 0:
                left[i] = left[i-1] + 1

    for i in range(n-1, -1, -1):
        if seats[i]==1:
            right[i] = 0
        else:
            if i<n-1:
                right[i] = right[i+1] + 1



    return max([min(left[i], right[i]) for i in range(n)])


print(maxDistToClosest([1,0,0,0,1,0,1]))
print(maxDistToClosest([1,0,0,0]))