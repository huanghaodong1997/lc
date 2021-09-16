from collections import defaultdict
class Solution:
    # N: length of words, M: length of each word
    # Time: O(N * M)
    
    def alienOrder(self, words) -> str:
        if not words: return ""
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        # used ch_set to store all exist characters
        ch_set = set(words[-1])
        edges = set()
        
        for i in range(len(words) - 1):
            ch_set |= set(words[i])
            
            # build graph, pointing from the first character that is different
            # from words[i] -> words[i + 1]
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    if (words[i][j], words[i + 1][j]) in edges:
                        break
                    graph[words[i][j]].append(words[i + 1][j])
                    indegree[words[i + 1][j]] += 1
                    edges.add((words[i][j], words[i + 1][j]))
                    break
                
                # edge cases, if the prefix j-1 characters equal
                # and len(words[i]) > len(words[i + 1])
                # invalid. E.g. "abc" should be larger than "ab"
                if j == min(len(words[i]), len(words[i + 1])) - 1 and len(words[i]) > len(words[i + 1]):
                    return ""
                    
        return self.kahnTopo(ch_set, indegree, graph, edges)

            
    def kahnTopo(self, ch_set, indegree, graph, edges):
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

    def dfsTopo(self, ch_set, graph):
        visited = set()
        temp = set()
        
        def helper(node):
            if node in visited or node in temp:
                return []
            temp.add(node)
            order = []
            for adj in graph[node]:
                if adj in temp:
                    # cycle
                    return []
                else:
                    order += helper(adj)
            visited.add(node)
            temp.remove(node)
            order.append(node)
            return order
        topo_order = []
        for node in ch_set:
            if node not in visited:
                topo_order += helper(node)
        if len(topo_order) != len(ch_set): return ""
        return "".join(topo_order[::-1])