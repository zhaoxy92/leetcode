def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    num2letter = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

    if len(digits) == 0:
        return []

    res = list(num2letter[int(digits[0])])

    if len(digits) == 1:
        return res

    for i in range(1, len(digits)):
        cur = list(num2letter[int(digits[i])])
        temp = []
        for l1 in res:
            for l2 in cur:
                temp.append(l1 + l2)
        res = temp

    return res