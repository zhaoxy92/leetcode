def totalFruit(tree):
    """
    :type tree: List[int]
    :rtype: int
    """

    if len(tree) < 3: return len(tree)
    dp = [1] * len(tree)
    record = {tree[-1]:len(tree)-1}
    for i in range(len(tree)-2, -1, -1):

        if tree[i] in record:
            dp[i] = dp[i+1] + 1
            record[tree[i]] = i
        else:
            if len(record) < 2:
                record[tree[i]] = i
                dp[i] = dp[i+1] + 1
            else:
                k,v = None, 0
                for kk in record:
                    if record[kk] > v:
                        k = kk
                        v = record[kk]
                record.pop(k)
                record[tree[i]] = i
                dp[i] = 1+v-(i+1)


    return max(dp)


print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))
print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))