from collections import defaultdict
class Solution:
    def getKey(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return tuple(count)
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            key = self.getKey(s)
            ans[key].append(s)
        return ans.values()

class AddAllAnagramInOrder:
    def getKey(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return tuple(count)
    def getAllAnagrams(self, strs):
        ans = []
        freq = defaultdict(int)
        for s in strs:
            key = self.getKey(s)
            freq[key] += 1
        for s in strs:
            key = self.getKey(s)
            if freq[key] > 1:
                ans.append(s)
        return ans
sol = AddAllAnagramInOrder()
arr = ["eat","tea","tan","ate","nat","bat"]
print(sol.getAllAnagrams(arr))