def wiggleSort(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    nums.sort()
    for i in range(1,len(nums)):
        if i%2==0:
            nums[i], nums[i-1] = nums[i-1], nums[i]

    return nums


print(wiggleSort([3,5,2,1,6,4]))