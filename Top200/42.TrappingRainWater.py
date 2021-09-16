class TwoPointerSolution:
    def trap(self, height) -> int:
        # Always bounded by the min of left max Length and right max length

        max_left = max_right = 0
        left, right = 0, len(height) - 1
        ans = 0
        
        while left < right:
            # Greedy intuitive, always want to inrease the lower side of the bar
            if height[left] < height[right]:
                if height[left] > max_left:
                    # The current idx could not store water
                    max_left = height[left]
                else:
                    ans += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    # The current idx could not store water
                    max_right = height[right]
                else:
                    ans += max_right - height[right]
                right -= 1
        return ans

# Stack Solution is O(n) Space, calculate the cumulative difference of bars