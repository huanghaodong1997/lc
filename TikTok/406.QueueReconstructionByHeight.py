
class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x:(-x[0], x[1]))
        output = []
        for p in people:
            # every people in output is taller or equal than p, so just insert into that pos
            output.insert(p[1], p)
        return output