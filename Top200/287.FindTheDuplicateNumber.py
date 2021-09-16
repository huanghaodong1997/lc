# size n + 1 array contain [1:n], must have duplicate
# use contradiction to proof

class NoExtraSpaceSolution:
    def findDuplicate(self, nums) -> int:
        # modify the array
        # o(1) space, o(n) time
        
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0: return num
            nums[num - 1] = -nums[num - 1]
        
# Reduce the problem to find linked list cycle node
#First of all, where does the cycle come from? Let's use the function f(x) = nums[x] to construct the sequence: x, nums[x], nums[nums[x]], nums[nums[nums[x]]], ....

# Each new element in the sequence is an element in nums at the index of the previous element.

# If one starts from x = nums[0], such a sequence will produce a linked list with a cycle.

# The cycle appears because nums contains duplicates. The duplicate node is a cycle entrance.

#index 0 1 2 3 4 5 6
#nums  2 6 4 1 3 1 5

# start from x = 2
# 2 -> 4 -> 3 -> [1]cycle! -> 6 -> 5 -> 1

class ConvertedToLinkedListCycleSolution:
    def findDuplicate(self, nums) -> int:
        # note that slow, fast is guarantee to be in the bound of nums
        # because num [1, n], size of nums = n + 1
        slow = fast = nums[0]
        
        # cycle must exist
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow