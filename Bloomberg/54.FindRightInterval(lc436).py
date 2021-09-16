class Solution:
    def findRightInterval(self, intervals):
        intvlIdx = {}
        n = len(intervals)
        ans = [-1] * n
        for i, interval in enumerate(intervals):
            intvlIdx[(interval[0], interval[1])] = i
        start_intvls = sorted(intervals, key=lambda x: x[0])
        end_intvls = sorted(intervals, key=lambda x: x[1])
        
        i = j = 0
        
        while i < n and j < n:
            e_intv = end_intvls[i]
            s_intv = start_intvls[j]
            if s_intv[0] < e_intv[1]:
                j += 1
            else:
                ans[intvlIdx[(e_intv[0], e_intv[1])]] = intvlIdx[(s_intv[0], s_intv[1])]
                i += 1
        return ans