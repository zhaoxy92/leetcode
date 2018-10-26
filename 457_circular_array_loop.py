def circularArrayLoop(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """


    mapping = {}
    visited = {i:False for i in range(len(nums))}
    for i in range(len(nums)):
        if visited[i]: continue
        cur = i
        while True:
            visited[cur] = True
            nxt = (cur + nums[cur])%len(nums)
            if nxt <0:
                nxt += len(nums)
            if nxt == cur or nums[nxt]*nums[cur]<0: break
            if nxt in mapping:
                return True
            mapping[cur] = nxt
            cur = nxt

    return False



print(circularArrayLoop( [2, -1, 1, 2, 2]))
print(circularArrayLoop( [-1, 2]))
print(circularArrayLoop([-2, 1, -1, -2, -2]))