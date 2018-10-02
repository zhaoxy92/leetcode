def lengthOfLongestSubstringTwoDistinct(s):

    best = 0
    queue = []
    size = 2
    for i in range(len(s)):
        c = s[i]
        if c in queue:
            queue.append(c)
        elif size>0:
            queue.append(c)
            size -= 1

        elif size==0 and not c in queue:
            if len(queue)>best:
                best = len(queue)
            while len(set(queue))>1:
                queue.pop(0)

            size += 1
            queue.append(c)
            size -= 1

    if len(queue) > best:
        best = len(queue)
    return best




print(lengthOfLongestSubstringTwoDistinct("eceba"))
print(lengthOfLongestSubstringTwoDistinct("ccaabbb"))
print(lengthOfLongestSubstringTwoDistinct("ababacccccc"))

