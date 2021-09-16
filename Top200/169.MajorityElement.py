class Solution:
    def majorityElement(self, nums) -> int:
        #If we had some way of counting instances of the majority element as +1+1 and instances of any other element as -1−1, summing them would make it obvious that the majority element is indeed the majority element.
        
        #voting algorithm
        
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
                
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate