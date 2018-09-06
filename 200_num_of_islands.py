def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    m = len(grid)
    n = len(grid[0])

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                DFS(grid, i, j)

    return count


def DFS(grid, i, j):
    m = len(grid)
    n = len(grid[0])

    grid[i][j] = 0

    if i-1>=0 and grid[i-1][j] == '1': DFS(grid, i-1, j)
    if i+1<m and grid[i+1][j] == '1': DFS(grid, i+1, j)
    if j-1>=0 and grid[i][j-1] == '1': DFS(grid, i, j-1)
    if j+1<n and grid[i][j+1] == '1': DFS(grid, i, j+1)


