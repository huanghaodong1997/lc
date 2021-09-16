from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes):
        count = defaultdict(list)
        for i,g in enumerate(groupSizes):
            count[g].append(i)
        
        ans = []
        
        for s in count:
            l = count[s]
            for i in range(0, len(l), s):
                ans.append(l[i:i+s])
        return ans
            
            