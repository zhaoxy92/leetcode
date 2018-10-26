def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    if len(matrix) == 0: return False

    m = len(matrix)
    n = len(matrix[0])

    if m == 1: return True


    i = 0
    row = matrix[0]
    while i<m-1:
        if not row[:n-1]==matrix[i+1][1:n]:
            return False
        row = matrix[i+1]

        i += 1
    return True

print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(isToeplitzMatrix([[11,74,0,93],[40,11,74,7]]))
