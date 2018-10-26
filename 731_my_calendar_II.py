class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start, end):
        for i, j in self.overlap:
            if (start<i and end>j) or i<=start<j or i<end<=j:
                return False

        for i, j in self.calendar:
            if (start<i and end>j) or i<=start<j or i<end<=j:
                self.overlap.append([max(start, i), min(end, j)])

        self.calendar.append([start, end])

        return True