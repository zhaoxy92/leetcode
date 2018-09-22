def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            if not j == i:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    for i in range(n):
        for j in range(n // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = temp
