from collections import defaultdict
from collections import deque
#O((M+N)⋅log ∗N)
# First of all, we iterate through each input equation and invoke union() upon it. As a result, the overall time complexity of this step is \mathcal{O}\big(N \cdot \log^{*}N\big)O(N⋅log 
# ∗
#  N).

# As the second step, we then evaluate the query one by one. For each evaluation, we invoke the find() function at most twice. Therefore, the overall time complexity of this step is \mathcal{O}\big(M \cdot \log^{*}N\big)O(M⋅log 
# ∗
#  N).

# To sum up, the total time complexity of the algorithm is \mathcal{O}\big( (M+N) \cdot \log^{*}N\big)O((M+N)⋅log 
# ∗
#  N).
class UFSolution:
    def calcEquation(self, equations, values, queries):
        gid_weight = {}
        #For example, "x / y = 2.0". Here, y is the parent of x; and the factor is 2.0.
        # If we also have "y / z = 3.0", which means that z is the final parent of x due to path compression; and the factor turns out to be 6.0.

        # When we find the parent of the string, we also accumulately multiply the factors
        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            parent_id, node_weight = gid_weight[node_id]
            
            if parent_id != node_id:
                new_parent_id, group_weight = find(parent_id)
                gid_weight[node_id] = (new_parent_id, node_weight * group_weight)
            
            return gid_weight[node_id]
        
        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together,
                # by attaching the dividend group to the one of divisor
                gid_weight[dividend_gid] = (divisor_gid, divisor_weight * value / dividend_weight)
                
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)
        results = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                # case 1). at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case 2). the variables do not belong to the same chain/group
                    results.append(-1.0)
                else:
                    # case 3). there is a chain/path between the variables
                    results.append(dividend_weight / divisor_weight)
        return results
#O(M⋅N)
# For each query, worse case you need to search the whole graph
class BFsSolution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for vertices, value in zip(equations, values):
            v1, v2 = vertices
            graph[v1].append((v2, value))
            graph[v2].append((v1, 1 / value))
        def find_path(src, dst):
            if src not in graph or dst not in graph: return -1
            q = deque([(src, 1.0)])
            visited = set()
            visited.add(src)
            while q:
                head, cur_res = q.popleft()
                if head == dst: return cur_res
                for adj, value in graph[head]:
                    if adj in visited: continue
                    q.append((adj, cur_res * value))
                    visited.add(adj)
            return -1.0
                    
        result = []
        for src, dst in queries:
            result.append(find_path(src, dst))
        return result