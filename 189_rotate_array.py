def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    k = k%len(nums)

    nums[:k],nums[k:] = nums[len(nums)-k:],nums[:len(nums)-k]

    return nums



def rotate2(nums, k):
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k)
    reverse(nums, k, len(nums)-1)

def reverse(nums, start, end):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1



