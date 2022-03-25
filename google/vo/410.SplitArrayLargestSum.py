class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # lower bound must be the maximum of nums
        l = max(nums)
        # upper bound is total sum of nums
        r = sum(nums)
        
        ans = r
        
        while l <= r:
            mid = (l + r) // 2
            cur_sum = 0
            
            cuts, curr_sum  = 0, 0
            for x in nums:
                curr_sum += x
                if curr_sum > mid:
                    cuts, curr_sum = cuts+1, x
            cnt = cuts + 1
                    
            if cnt <= m:
                ans = mid
                
                # mid too big, so few groups
                r = mid - 1
            else:
                l = mid + 1
        return ans
