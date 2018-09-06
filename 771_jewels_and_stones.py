def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """

    if J == '' or S=='': return 0
    record = {}
    for j in J:
        record[j] = 0

    for s in S:
        if s in record:
            record[s] += 1

    if len(record)>0:
        return sum(record.values())
    return 0

print(numJewelsInStones(J = "aA", S = "aAAbbbb"))
print(numJewelsInStones(J = "z", S = "ZZ"))