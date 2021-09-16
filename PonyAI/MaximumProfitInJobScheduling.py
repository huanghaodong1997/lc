import bisect
class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])
        n = len(jobs)
        
        sortedStartTime = [job[0] for job in jobs]
        
        dp = [0] * n
        dp[n - 1] = jobs[n - 1][2]
        for i in range(n - 2, -1, -1):
            endTime = jobs[i][1]
            cur_profit = jobs[i][2]
            
            # next start time must be larger or equal than endTime, can use binary search here.
            next_idx = bisect.bisect_left(sortedStartTime, endTime, i + 1, n)
            take = dp[next_idx] + cur_profit if next_idx < n else cur_profit
            dp[i] = max(take, dp[i + 1])
        return dp[0]
        