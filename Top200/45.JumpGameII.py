class Solution:
    def jump(self, nums) -> int:
        if len(nums) < 2:
            return 0
        max_pos = max_step = nums[0]
        step = 1
        #max_steps variable to track the maximum position reachable during the current jump
        for i, num in enumerate(nums):
            if i > max_step:
                # Greedy, only increase step when you need to move
                # you can jump from  between previous index and current index by 1 step
                # to gain max_step == max_pos
                # So you are good to go
                step += 1
                max_step = max_pos
            max_pos = max(max_pos, i + num)
        return step
# if you want to remember the path, just store index when you update max_pos