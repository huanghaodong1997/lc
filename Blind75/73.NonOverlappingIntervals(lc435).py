class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort()
        i, prev = 1, 0
        res = 0
        while i < len(intervals):
            # overlap
            if intervals[prev][1] > intervals[i][0]:
                # always choose to keep the interval that has smaller end time
                if intervals[prev][1] > intervals[i][1]:
                    prev = i
                res += 1
            else:
                prev = i
            i += 1
                
        return res