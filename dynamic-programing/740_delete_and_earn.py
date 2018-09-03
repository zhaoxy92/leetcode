from collections import Counter

def deleteAndEarn(nums):
    """
    :type nums: List[int]
    :rtype: int
    """



    candidates = sorted(list(set(nums)))
    points = Counter(nums)

    use = [0] * len(candidates)
    avoid = [0] * len(candidates)

    use[0] = candidates[0] * points[candidates[0]]
    pre = candidates[0]

    for i in range(1, len(candidates)):

        if not candidates[i] - 1 == pre:
            avoid[i] = max(avoid[i-1], use[i-1])
            use[i] = candidates[i]*points[candidates[i]]+ max(avoid[i-1], use[i-1])
        else:
            avoid[i] = max(avoid[i-1], use[i-1])
            use[i] = avoid[i-1] + candidates[i]*points[candidates[i]]

        pre = candidates[i]

    return max(use[-1], avoid[-1])

print(deleteAndEarn([3,4,2]))
print(deleteAndEarn([2, 2, 3, 3, 3, 4]))
