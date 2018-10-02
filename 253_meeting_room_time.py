def minMeetingRooms(intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """

    start = []
    end = []
    for intv in intervals:
        start.append(intv[0])
        end.append(intv[1])
    start = sorted(start)
    end = sorted(end)

    end_point = 0
    ans = 0
    for i in range(len(start)):
        if start[i] < end[end_point]:
            ans += 1
        else:
            end_point += 1
    return ans

print(minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(minMeetingRooms([[7,10],[2,4]]))
print(minMeetingRooms([[9,10],[4,9],[4,17]]))