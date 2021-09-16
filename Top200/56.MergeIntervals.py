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


#First, we sort the list as described. Then, 
# we insert the first interval into our merged list 
# and continue considering each interval in turn as follows: 
# If the current interval begins after the previous interval ends, 
# then they do not overlap and we can append the current interval to merged. 
# Otherwise, they do overlap, and we merge them by updating the end of the previous
# terval if it is less than the end of the current interval.