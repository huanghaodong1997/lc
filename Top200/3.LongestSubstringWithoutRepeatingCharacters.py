class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        i = j = 0
        res = 0
        while j < len(s):
            while i < j and s[j] in window:
                window.remove(s[i])
                i += 1
            res = max(res, j - i + 1)
            window.add(s[j])
            j += 1
        return res
# We can maintain a window set, each character in this window is unique
# and we can use two pointer to represent the left bound and right
# bound of window, the right pointer will keep moving toward right
# When right pointer move to a position, if the character in current
# position exist in window set, we will shrink the left pointer and 
# remove every character that is not in the window from the window set
