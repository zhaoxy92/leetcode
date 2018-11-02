import random
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum = [0] * len(w)
        self.sum[0] = w[0]
        for i in range(1, len(w)):
            self.sum[i] = self.sum[i - 1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """

        total = self.sum[-1]
        rand = random.randint(1, total)
        left, right = 0, len(self.sum) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if rand >= self.sum[mid]:
                left = mid
            else:
                right = mid
        if rand <= self.sum[left]:
            return left
        return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()