def partitionDisjoint(A):
    """
    :type A: List[int]
    :rtype: int
    """
    if len(A)==2: return 1

    ans = 1
    left_max = A[0]
    right_min = min(A[1:])


    for i in range(1, len(A)-1):
        if A[i-1] > left_max:
            left_max = A[i-1]
        if A[i-1] == right_min:
            right_min = min(A[i:])

        if left_max <= right_min:
            return i

    return len(A)-1


print(partitionDisjoint([5,0,3,8,6]))
print(partitionDisjoint([1,1,1,0,6,12]))
print(partitionDisjoint([1,1]))
print(partitionDisjoint([32,57,24,19,0,24,49,67,87,87]))
print(partitionDisjoint([26,51,40,58,42,76,30,48,79,91]))