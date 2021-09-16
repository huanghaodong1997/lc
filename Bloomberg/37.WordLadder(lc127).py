from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        all_comb = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                intermediate = word[:i] + '*' + word[i + 1:]
                all_comb[intermediate].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while q:
            word, level = q.popleft()
            if word == endWord: return level
            for i in range(L):
                intermidate = word[:i] + '*' + word[i + 1:]
                for next_word in all_comb[intermidate]:
                    if next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, level + 1))
        return 0
                    
            