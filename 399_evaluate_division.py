import collections
def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    record = collections.defaultdict(lambda: collections.defaultdict(int))
    for (var1, var2), v in zip(equations, values):
        record[var1][var2] = v
        record[var2][var1] = 1.0 / v

    for i in record:
        record[i][i] = 1
        for j in record:
            for k in record:
                if record[j][i] and record[i][k]:
                    record[j][k] = record[j][i] * record[i][k]
                else:
                    record[j][k] = -1
    res = []
    for q in queries:
        res.append(record[q[0]][q[1]])

    return res


print(calcEquation([["a","b"],["e","f"],["b","e"]], [3.4,1.4,2.3], [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))
print(calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))