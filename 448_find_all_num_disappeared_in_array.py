def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    for i in range(len(nums)):
        cur = abs(nums[i])
        nums[cur-1] = -abs(nums[cur-1])
    res = []
    for i in range(len(nums)):
        if nums[i]>0:
            res.append(i+1)
    return res

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))