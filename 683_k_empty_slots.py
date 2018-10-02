def kEmptySlots(flowers, k):
    """
    :type flowers: List[int]
    :type k: int
    :rtype: int
    """

    N = len(flowers)
    record = {i: False for i in range(N)}

    for i in range(N):
        pos = flowers[i]-1

        record[pos] = True

        left = pos-1
        while left>=0 and not record[left]:
            left -= 1

        right = pos+1
        while right<=N-1 and not record[right]:
            right += 1

        if (left>=0 and pos-left-1==k) or (right<=N-1 and right-pos-1==k):
            return i+1

    return -1


print(kEmptySlots([1,3,2], 1))
print(kEmptySlots([1,2,3], 1))