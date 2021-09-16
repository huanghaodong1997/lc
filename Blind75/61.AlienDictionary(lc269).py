from collections import defaultdict
class Solution:
    # N: length of words, M: length of each word
    # Time: O(N * M)
    
    def alienOrder(self, words) -> str:
        if not words: return ""

        graph = defaultdict(set)
        indegree = defaultdict(int)
        ch_set = set(words[-1])
        edges = set()
        
        for i in range(len(words) - 1):
            ch_set |= set(words[i])
            
            # build graph
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    if (words[i][j], words[i + 1][j]) in edges:
                        break
                    graph[words[i][j]].add(words[i + 1][j])
                    indegree[words[i + 1][j]] += 1
                    edges.add((words[i][j], words[i + 1][j]))
                    break
                
                # edge cases
                if j == min(len(words[i]), len(words[i + 1])) - 1 and len(words[i]) > len(words[i + 1]):
                    return ""
                    
                
        q = []
        res = ""
        for node in ch_set:
            if indegree[node] == 0:
                q.append(node)

        while q:
            node = q.pop(0)
            res += node
            for adj in graph[node]:
                
                edges.remove((node, adj))
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
                    

        if edges:
            return ""
        else: 
            return res
            
        