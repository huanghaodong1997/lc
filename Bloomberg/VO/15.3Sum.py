class NoSortSolution:
    def threeSum(self, nums):
        #Instead of re-populating a hashset every time in the inner loop, we can use a hashmap and
        #  populate it once. Values in the hashmap will indicate whether we have
        #  encountered that element in the current iteration. When we process nums[j] in the inner loop, 
        # we set its hashmap value to i. This indicates that we can now use nums[j] as a complement for nums[i].
        res, dups = set(), set()
        seen = {}
        
        for i, val1 in enumerate(nums):
            # prevent duplication
            if val1 not in dups:
                dups.add(val1)
                
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    # seen[complement] = i means that u have meet the complement in nums[i+1:i+j-1]
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1,val2,complement))))
    
                    seen[val2] = i
        return list(res)

class SortO1Solution:
    def threeSum(self, nums):
        # sort the arra
        # skip the duplicates element
        
        res = []
        nums.sort()
        
        def twoSum(nums, i, res):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum < 0:
                    lo += 1
                elif sum > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # important: remove dupliacates tuples
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
            
        
        for i in range(len(nums)):
            if nums[i] > 0: 
                # If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(nums, i, res)
        return res
    