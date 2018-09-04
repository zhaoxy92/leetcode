def canPartitionKSubsets(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    if not sum(nums)%k==0: return False

    target = sum(nums)//k

    

