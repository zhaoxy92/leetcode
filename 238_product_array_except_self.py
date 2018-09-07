def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    output = [1] * len(nums)

    left = 1
    for i in range(len(nums)-1):
        left  *= nums[i]
        output[i+1] *= left

    right = 1
    for i in range(len(nums)-1, 0, -1):
        right *= nums[i]
        output[i-1] *= right

    return output

print(productExceptSelf([1,2,3,4]))