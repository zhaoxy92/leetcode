def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    num2idx = {}
    for i in range(len(numbers)):
        if numbers[i] in num2idx:
            num2idx[numbers[i]].append(i+1)
        else:
            num2idx[numbers[i]] = [i+1]

    for n in numbers:
        if target-n in num2idx:
            return [min(num2idx[n][0], num2idx[target-n][-1]), max(num2idx[n][0], num2idx[target-n][-1])]

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    s = 0
    e = len(numbers)-1
    while s<e:
        t = numbers[s] + numbers[e]
        if t == target:
            return [s+1, e+1]
        elif t>target:
            e -= 1
        else:
            s += 1

print(twoSum([2,7,11,15], 9))
print(twoSum([0,0,3,4], 0))