ans = []
def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    # max_h = [item[0] for item in people]
    find(people, ans)
    return ans

def find(lst, ans):
    max_h = [item[0] for item in lst]
    if lst:
        lst = sorted(lst, key=lambda x:(x[1], x[0]))
        ans.append(lst[0])
        for i in range(len(lst)):
            if lst[i][0] < lst[0][0]:
                lst[i][1] -= 1
        find(lst[1:], ans)



print(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))

