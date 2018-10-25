def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    cnt = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                if i==0 or grid[i-1][j]==0:
                    cnt += 1
                if i==m-1 or grid[i+1][j]==0:
                    cnt += 1
                if j==0 or grid[i][j-1]==0:
                    cnt += 1
                if j==n-1 or grid[i][j+1]==0:
                    cnt += 1

    return cnt



print(islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
))

