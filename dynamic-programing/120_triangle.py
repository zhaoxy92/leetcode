def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """


    for i in range(1, len(triangle)):
        for j in range(triangle[i][j]):

            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            else:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j] + triangle[i - 1][j - 1]

    return max(triangle[-1])

p