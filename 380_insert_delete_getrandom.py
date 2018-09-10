import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        data = []
        record = {}
        length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        if not val in self.record:
            self.data.append(val)
            self.record[val] = self.length
            self.length += 1
            return True
        else:
            return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.record:
            idx = self.record[val]
            last = self.data[self.length-1]
            self.data[idx] = last
            self.record[last] = idx
            del self.record[val]
            self.length -= 1

            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """

        idx = random.randint(0, self.length-1)
        return self.data[idx]


        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()