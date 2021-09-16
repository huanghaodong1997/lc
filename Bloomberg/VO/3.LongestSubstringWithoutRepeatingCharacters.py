class Solution:
    # If a substring sij
# ​	
#   from index ii to j−1 is already checked to have no duplicate characters. 
# We only need to check if s[j] is already in the substring si
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        i = j = 0
        res = 0
        while j < len(s):
            # We use HashSet to store the characters in 
            # current window [i, j)[i,j) (j = ij=i initially). Then we slide the index jj 
            # to the right. If it is not in the HashSet, we slide jj further. 
            # Doing so until s[j] is already in the HashSet. At this point, 
            # we found the maximum size of substrings without duplicate characters start with index ii.
            # Then we shrink the pointer i until s[j] is not in the window
            while i < j and s[j] in window:
                window.remove(s[i])
                i += 1
            res = max(res, j - i + 1)
            window.add(s[j])
            j += 1
        return res