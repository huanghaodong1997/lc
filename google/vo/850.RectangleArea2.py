class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        points = []
        
        # sort by x, and we want each point to keep the information of height of this rectangle
        for x1, y1, x2, y2 in rectangles:
            points.append((x1, 0, y1, y2))
            points.append((x2, 1, y1, y2))
            
        points.sort()
        
        def merge(intervals):
            ans = []
            for beg, end in sorted(intervals):
                if not ans or ans[-1][1] < beg:
                    ans += [[beg, end]]
                else:
                    ans[-1][1] = max(ans[-1][1], end)
            return sum(j - i for i, j in ans)
        
        intervals, ans, prev_x = [], 0, points[0][0]
        
        for x, op, y1, y2 in points:
            # Don't actually modify the intervals
            # as long as (y1, y2) is in the intervals, we know how many valid height we have from prev_x ~ x
            ans += merge(intervals) * (x - prev_x)
            if op == 0:
                intervals.append((y1, y2))
            else:
                intervals.remove((y1, y2))
            prev_x = x
        return ans % (10**9 + 7)