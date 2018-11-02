def __init__(self, A):
    """
    :type A: List[int]
    """
    self.A = A
    self.index = 0


def next(self, n):
    """
    :type n: int
    :rtype: int
    """
    while self.index < len(self.A) and self.A[self.index] < n:
        n -= self.A[self.index]
        self.index += 2
    if self.index >= len(self.A):
        return -1
    self.A[self.index] -= n
    return self.A[self.index + 1]