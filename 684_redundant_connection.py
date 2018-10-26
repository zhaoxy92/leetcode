def findRedundantConnection(edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """


    mapping = {}
    for e in edges:
        seen = []
        if e[0] in mapping and e[1] in mapping and isconnected(e[0],e[1], mapping, seen):
            return e

        if e[0] in mapping:
            mapping[e[0]].append(e[1])
        else:
            mapping[e[0]] = [e[1]]
        if e[1] in mapping:
            mapping[e[1]].append(e[0])
        else:
            mapping[e[1]] = [e[0]]

    print(mapping)

def isconnected(u, v, graph, history):
    if not u in history:
        history.append(u)
        if u == v:
            return True
        else:
            return any(isconnected(ui, v, graph, history) for ui in graph[u])
    return False

print(findRedundantConnection([[1,2], [1,3], [2,3]]))
print(findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))
print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
print(findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))