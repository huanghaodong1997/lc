class Solution:
    def merge(self, intervals):
        if not intervals: return []
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            
            if s > ans[-1][1]:
                ans.append([s, e])
            else:
                ans[-1][1] = max(e, ans[-1][1])
        return ans