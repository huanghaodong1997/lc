class Solution:
    # [2, 3, -2, -4]
    # [1, 2, 3, 4]
    # [2, 3, -2, 8]

    # We are utilizing the previous calculate result
    # Let dp_max[i] = maximum product subarray ending with i
    # max(dp_max) is the answer we want

    # If nums[i] < 0, we might use dp_min[i - 1] * nums[i] to 
    # Get a big value. And vise versa we can get dp_min[i] using dp_max[i-1]

    #So dp_max[i] = max(dp_max[i - 1] * nums[i],...)
    #. ..
    
    # Now We observer that we are only using the previous result
    # So we can just use two variable to store the calculated result

    def maxProduct(self, nums) -> int:
       
        ans = max_p = min_p = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]

            # use temp variable here to prevent result interrupting
            t_max_p = max(max_p * num, min_p * num, num)
            t_min_p = min(min_p * num, max_p * num, num)
            max_p = t_max_p
            min_p = t_min_p
            ans = max(ans, max_p, min_p)
        return ans