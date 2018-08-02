def wiggleMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) <=2:
        return len(nums)

    up = [0]*len(nums)
    dw = [0]*len(nums)
    up[0] = 1
    dw[0] = 1

    for i in range(1, len(nums)):
        for j in range(i):

            if nums[i] > nums[j]:
                up[i] = max(up[i], dw[j]+1)
            elif nums[i] < nums[j]:
                dw[i] = max(dw[i], up[j]+1)

    return max(up[-1], dw[-1])

def wiggleMaxLength2(nums):
    if len(nums) <= 2:
        return len(nums)

    up = [0] * len(nums)
    dw = [0] * len(nums)
    up[0] = 1
    dw[0] = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            up[i] = dw[i-1] + 1
            dw[i] = dw[i-1]
        elif nums[i] < nums[i-1]:
            up[i] = up[i-1]
            dw[i] = up[i-1] + 1
        else:
            up[i] = up[i-1]
            dw[i] = dw[i-1]

    return max(up[-1], dw[-1])

print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(wiggleMaxLength([0,0,0]))

print(wiggleMaxLength2([1,17,5,10,13,15,10,5,16,8]))