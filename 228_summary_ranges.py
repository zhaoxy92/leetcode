def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums) == 0: return []
    ans = []
    s = 0
    e = 0

    for i in range(len(nums)-1):
        if nums[i+1]-nums[i]==1:
            e = i+1
        else:
            if not s == e:
                ans.append(str(nums[s]) + '->' + str(nums[e]))
            else:
                ans.append(str(nums[s]))

            s = i+1
            e = i+1

    if not s == len(nums)-1:
        ans.append(str(nums[s]) + '->' + str(nums[e]))
    else:
        ans.append(str(nums[s]))
    return ans


print(summaryRanges([0,2,3,4,6,8,9]))
print(summaryRanges([0,1,2,4,5,7]))