import random

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    # Quick select

    pivot = random.choice(nums)
    left = []
    right = []
    same = []

    for i in range(len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        elif nums[i] > pivot:
            right.append(nums[i])
        else:
            same.append(nums[i])


    if len(right) >= k:
        return findKthLargest(right, k)
    elif len(right)+len(same) >=k:
        return pivot
    else:
        return findKthLargest(left, k-len(right)-len(same))



print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([-1,-1], 2))