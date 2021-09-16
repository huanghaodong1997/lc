
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for employee in schedule:
            for s in employee:
                intervals.append((s.start, 0))
                intervals.append((s.end, 1))
        intervals.sort()
        balance = 0
        prev = None
        ans = []
        for t, op in intervals:
            if prev != None and balance == 0:
                ans.append(Interval(prev, t))
            if op == 0:
                balance += 1
            elif op == 1:
                balance -= 1
            prev = t
        return ans