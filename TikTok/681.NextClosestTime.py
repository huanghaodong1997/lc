import itertools
class Solution:
    def nextClosestTime(self, time: str) -> str:
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        
        for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                candidate = (cur - start) % (24 * 60)
                if 0 < candidate < elapsed:
                    ans = cur
                    elapsed = candidate
        
        h = ans // 60
        m = ans % 60
        
        h_str = str(h) if h >= 10 else '0' + str(h)
        m_str = str(m) if m >= 10 else '0' + str(m)
        return h_str + ':' + m_str