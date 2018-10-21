def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """


    digits[-1] = digits[-1] + 1 if digits[-1]<9 else 0
    flag = True if digits[-1] == 0 else False

    i = len(digits)-2
    while i>=0:
        if flag:
            digits[i] += 1
            digits[i] = 0 if digits[i]==10 else digits[i]
            flag = True if digits[i] == 0 else False

            i -= 1

        else:
            break

    if flag:
        digits.insert(0,1)
    return  digits

print(plusOne([4,3,2,1]))
print(plusOne([1,2,3]))
print(plusOne([9]))
print(plusOne([3,3,9]))