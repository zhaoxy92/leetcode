def findReplaceString(S, indexes, sources, targets):
    """
    :type S: str
    :type indexes: List[int]
    :type sources: List[str]
    :type targets: List[str]
    :rtype: str
    """

    comb = [(indexes[i], sources[i], targets[i]) for i in range(len(indexes))]
    comb = sorted(comb, key=lambda x:x[0])

    indexes = [x[0] for x in comb]
    sources = [x[1] for x in comb]
    targets = [x[2] for x in comb]

    # print(indexes)
    # print(sources)
    # print(targets)
    ans = ''
    pre = 0
    for i in range(len(indexes)):
        ans += S[pre:indexes[i]]
        if S[indexes[i]:].startswith(sources[i]):
            ans += targets[i]
            pre = indexes[i] + len(sources[i])
        else:
            if i < len(indexes)-1:
                ans += S[indexes[i]:indexes[i+1]]
                pre = indexes[i+1]

    ans += S[pre:]

    return ans

print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]))
print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]))

print(findReplaceString(S = "vmokgggqzp", indexes=[3,5,1], sources=["kg","ggq","mo"], targets=["s","so","bfr"]))
print(findReplaceString(S="jjievdtjfb", indexes=[4,6,1], sources=["md","tjgb","jf"], targets=["foe","oov","e"]))