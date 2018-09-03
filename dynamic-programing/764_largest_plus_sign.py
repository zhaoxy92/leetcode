def orderOfLargestPlusSign(N, mines):
    """
    :type N: int
    :type mines: List[List[int]]
    :rtype: int
    """


    up = [[1 for _ in range(N)] for _ in range(N)]
    down = [[1 for _ in range(N)] for _ in range(N)]
    left = [[1 for _ in range(N)] for _ in range(N)]
    right = [[1 for _ in range(N)] for _ in range(N)]


    for mine in mines:
        up[mine[0]][mine[1]] = 0
        down[mine[0]][mine[1]] = 0
        left[mine[0]][mine[1]] = 0
        right[mine[0]][mine[1]] = 0

    for i in range(1, N):
        for j in range(N):
            if not up[i][j]==0:
                up[i][j] = up[i-1][j] + 1

    for i in range(N-2, -1,-1):
        for j in range(N):
            if not down[i][j] == 0:
                down[i][j] = down[i + 1][j] + 1

    for i in range(N):
        for j in range(1, N):
            if not left[i][j] == 0:
                left[i][j] = left[i][j-1] + 1


    for i in range(N):
        for j in range(N-2, -1, -1):
            if not right[i][j] == 0:
                right[i][j] = right[i][j+1] + 1

    ans = 0
    for i in range(N):
        for j in range(N):
           ans = max(ans, min(up[i][j], down[i][j], left[i][j], right[i][j]))


    return ans

print(orderOfLargestPlusSign(5,[[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0],[2,1],[2,3],[2,4],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[4,4]]))
print(orderOfLargestPlusSign(5, [[3,0],[3,3]]))
print(orderOfLargestPlusSign(5, [[3,0], [3,3]]))
print(orderOfLargestPlusSign(5, [[4,2]]))
print(orderOfLargestPlusSign(2, []))
print(orderOfLargestPlusSign(1, [[0,0]]))