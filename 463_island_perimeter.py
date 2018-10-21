def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    # cnt = 0
    # m = len(grid)
    # n = len(grid[0])
    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j]==1:
    #             if i==0 or grid[i-1][j]==0:
    #                 cnt += 1
    #             if i==m-1 or grid[i+1][j]==0:
    #                 cnt += 1
    #             if j==0 or grid[i][j-1]==0:
    #                 cnt += 1
    #             if j==n-1 or grid[i][j+1]==0:
    #                 cnt += 1
    #
    # return cnt

    m = len(grid)
    n = len(grid[0])
    visited = [[False]*n for _ in range(m)]
    stack = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                stack.append([i,j])
                visited[i][j] = True
            break
        if len(stack)>0:
            break
    if len(stack)==0: return 0

    while stack:
        cur = stack.pop()
        if cur[0]==0 and





print(islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
))

