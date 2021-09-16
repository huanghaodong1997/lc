# 等价于 subarray sum equal k

# O(n) Time, O(n) Space
class Solution:
    def numSubarraysWithSum(self, A, S: int) -> int:
        mp = {0:1}
        cur_sum = 0
        res = 0
        for num in A:
            cur_sum += num
            if cur_sum - S in mp:
                res += mp[cur_sum - S]
            if cur_sum not in mp:
                mp[cur_sum] = 0
            mp[cur_sum] += 1
        return res
# O(n) Time, O(1) Space
# For each j, try to count the number of i's that have the subarray[i,j]
# equal to S
# 注意这个方法只有在这道题才适用，subarray sum equal k 不行
class Solution2:
    def numSubarraysWithSum(self, A, S: int) -> int:
        i_lo = i_hi = 0
        sum_lo = sum_hi = 0
        ans = 0
        for j, num in enumerate(A):
            # Maintain the left pointer i_lo to ensure sum less or equal than S
            sum_lo += num
            while i_lo < j and sum_lo > S:
                sum_lo -= A[i_lo]
                i_lo += 1
            
            # Maintain the right pointer i_hi to get the window res
            sum_hi += num
            while i_hi < j and (sum_hi > S or sum_hi == S and A[i_hi] == 0):
                sum_hi -= A[i_hi]
                i_hi += 1
            # This mean we are good to go
            if sum_lo == S:
                ans += i_hi - i_lo + 1
        return ans