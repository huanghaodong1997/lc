from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        all_comb = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                intermediate = word[:i] + '*' + word[i + 1:]
                all_comb[intermediate].append(word)
        
        # All key in this dict must have an ancestor BeginWord
        # Key: a child node
        # value: parents
        parent = defaultdict(set)
        
        # Starting from beginWord
        q = deque([(beginWord, 1)])

        while q:
            size = len(q)
            
            # use local variable to record the next level parent map
            # because in the current level there may be multiple nodes
            # point to a same node
            next_level = defaultdict(set)
            for _ in range(size):
                word, level = q.popleft()
                for i in range(L):
                    intermidate=word[:i] + '*' + word[i + 1:]
                    for next_word in all_comb[intermidate]:
                        # avoid adding longer path to res
                        if next_word not in parent:
                            next_level[next_word].add(word)
                            q.append((next_word, level + 1))
            parent.update(next_level)
        res = [[endWord]]
        
        # rebuild the path
    
        # Because the technique we are using above 'local visited' approach
        # We can ensure that the value of parent will definitely be in the final path
        # So we can rebuild the path from endWord
        while res and res[0][0] != beginWord:
            tmp = []
            for r in res:
                curr_word = r[0]
                for p in parent[curr_word]:
                     tmp.append([p] + r[:])
            res = tmp
                
        
        
        return res