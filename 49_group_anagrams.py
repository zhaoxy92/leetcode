import collections
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    record = collections.defaultdict(list)
    for s in strs:
        record[''.join(sorted(s))].append(s)

    return list(record.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
