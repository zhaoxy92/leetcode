def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """


    k = k%len(nums)
    for _ in range(k):
        


print(rotate([1,2,3,4,5,6,7],3))
print(rotate([1,2],3))

