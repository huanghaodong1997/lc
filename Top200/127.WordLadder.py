from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # Consider this problem a graph problem
        # We have to reach from the start node to the end node 
        # using some intermediate nodes/words. 
        # The intermediate nodes are determined by the wordList 
        # given to us. The only condition for every step we take on 
        # this ladder of words is the current word should change by 
        # just one letter.

        #We will essentially be working with an undirected and 
        # unweighted graph with words as nodes and edges between 
        # words which differ by just one letter.

        # Different words are connected by intermediates node
        # such as   Dog - D*g - Dig
        intermediates = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                intermediates[pattern].append(word)
        level = 1
        q = [beginWord]
        visited = set()
        while q:
            size = len(q)
            for _ in range(size):
                word = q.pop(0)
                if word == endWord:
                    return level
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for candi in intermediates[pattern]:
                        if candi in visited: continue
                        visited.add(candi)
                        q.append(candi)
            level += 1
        return 0