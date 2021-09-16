class Solution:
    def minMeetingRooms(self, intervals) -> int:
        events = []
        for time in intervals:
            events.append((time[0], 1))
            events.append((time[1], 0))
        events.sort()
        res = 0
        rooms = 0
        for time, op in events:
            if op == 1:
                rooms += 1
            else:
                rooms -= 1
            res = max(res, rooms)
        return res
        