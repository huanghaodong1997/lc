from collections import defaultdict
import heapq
categories = [
"House Painting,Interior Painting,0.9",
"Handyman,Massage Therapy,0.1",
"Handyman,House Painting,0.5",
"House Painting,House Cleaning,0.7",
"Furniture Assembly,Handyman,0.8",
"Furniture Assembly,Massage Therapy,0.1",
"Plumbing Drain Repair,Junk Removal,0.3",
]

projects = ["Plumbing Drain Repair",
"Furniture Assembly",
"Massage Therapy"]

from collections import defaultdict
import heapq
class Element:
    def __init__(self, score, project):
        self.score = score
        self.project = project
    def __lt__(self, ot):
        if self.score < ot.score:
            return True
        elif self.score > ot.score:
            return False
        else:
            return self.project < ot.project


def categorySuggestions(categories, projects, k):
    # Write your code here
    graph = defaultdict(list)
    for s in categories:
        p1, p2, score = s.split(",")
        graph[p1].append((float(score), p2))
        graph[p2].append((float(score), p1))
        
    h = []
    res = []
    for p in projects:
        for score, adj in graph[p]:
            heapq.heappush(h, (-score, adj))
        heapq.heappush(h, (-1.0, p))
        tmp_set = set()
        next_h = []
        tmp_k = k
        tmp_res = []
        while tmp_k > 0 and h:
            a = heapq.heappop(h)
            score, proj = a
            if proj not in tmp_set:
                tmp_set.add(proj)
                tmp_res.append(proj)
                heapq.heappush(next_h, (score, proj))
                tmp_k -= 1
        h = next_h[:]
        res.append(tmp_res)

    return res


print(categorySuggestions(categories, projects, 2))