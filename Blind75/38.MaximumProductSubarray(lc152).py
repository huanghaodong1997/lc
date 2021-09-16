class Solution:
    # [2, 3, -2, -4]
    # [1, 2, 3, 4]
    # [2, 3, -2, 8]

    # Time: O(n)
    # Space: O(1)
    def maxProduct(self, nums) -> int:
       
        ans = max_p = min_p = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            t_max_p = max(max_p * num, min_p * num, num)
            t_min_p = min(min_p * num, max_p * num, num)
            max_p = t_max_p
            min_p = t_min_p
            ans = max(ans, max_p, min_p)
        return ans