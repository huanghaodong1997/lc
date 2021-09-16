# Create dictionary using each friend as keys and a list of people they are closer to than the person they are paired with as values. This can be done using index.

# Then use nested for loop to find when people are on each other's list.
class Solution:
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        prefer = {}
        
        for p1, p2 in pairs:
            prefer[p1] = preferences[p1][:preferences[p1].index(p2)]
            prefer[p2] = preferences[p2][:preferences[p2].index(p1)]
        ans = 0
        for i in prefer:
            for j in prefer[i]:
                if i in prefer[j]:
                    ans += 1
                    break
        return ans