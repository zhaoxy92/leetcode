def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    origin = [0, 0]
    for m in moves:
        if m == 'R':
            origin[1] += 1
        if m == 'L':
            origin[1] -= 1
        if m == 'U':
            origin[0] += 1
        if m == 'D':
            origin[0] -= 1
    return origin[0] == 0 and origin[1] == 0