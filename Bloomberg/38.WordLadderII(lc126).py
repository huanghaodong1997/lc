from collections import defaultdict
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        all_comb = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                intermediate = word[:i] + '*' + word[i + 1:]
                all_comb[intermediate].append(word)
        ans = []
        parent = {}
        q = deque([(beginWord, 1, [beginWord])])
        final_level = float('inf')
        visited = set()
        visited.add(beginWord)

        while q:
            size = len(q)
            local_visited = set()
            for _ in range(size):
                word, level, path = q.popleft()
                visited.add(word)
                for i in range(L):
                    intermidate=word[:i] + '*' + word[i + 1:]
                    for next_word in all_comb[intermidate]:
                        if next_word == endWord and level <= final_level:
                            final_level = min(level, final_level)
                            ans.append(path + [endWord])

                        if next_word not in visited:
                            local_visited.add(next_word)
                            parent[next_word] = word
                            q.append((next_word, level + 1, path + [next_word]))
            visited.union(local_visited)                            
        return ans
