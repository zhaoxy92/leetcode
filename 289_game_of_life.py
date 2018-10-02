def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    #1: 1 or 2
    #0: 0 or -1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1: board[i][j] = count(board, i, j) + 1
            else: board[i][j] = -count(board, i, j)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in [3, 4, -3]: board[i][j] = 1
            else: board[i][j] = 0




def count(board, x, y):
    cnt = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
           if i>=0 and i<len(board) and j>=0 and j < len(board[0]) and board[i][j] > 0:
               cnt += 1
    return cnt