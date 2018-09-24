def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    if len(height) == 0: return 0

    leftmost = [0] * len(height)
    rightmost = [0] * len(height)

    leftmost[0] = height[0]
    for i in range(1, len(height)):
        leftmost[i] = max(leftmost[i - 1], height[i])

    rightmost[-1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
        rightmost[i] = max(rightmost[i + 1], height[i])

    s = 0
    for i in range(len(height)):
        s = s + min(leftmost[i], rightmost[i]) - height[i]
    return s