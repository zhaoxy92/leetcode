class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.record = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        self.data.append(x)
        if len(self.record) == 0 or x <= self.record[-1]:
            self.record.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.data) == 0: return
        v = self.data.pop()
        if v == self.record[-1]:
            self.record.pop()

        return v

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.record[-1]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()