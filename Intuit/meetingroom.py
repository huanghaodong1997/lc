meetings = [[845,915], [1515, 1545], [1230,1300],[845,900],[1300,1500],[930,1200],[1600,2359]]
def canSchedule(meetings, start, end):
    for s, e in meetings:
        if (start >= s and start < e) or (end > s and end <= e) \
            or (start < s and end > e):
            return False
    return True
#print(canSchedule(meetings, 1450, 1500))

def merge(meetings):
    if not meetings: return []
    meetings.sort()
    ans = [meetings[0]]
    for i in range(1, len(meetings)):
        s, e = meetings[i]
        
        if s > ans[-1][1]:
            ans.append([s, e])
        else:
            ans[-1][1] = max(e, ans[-1][1])
    return ans

def free_time(meetings):
    meetings = merge(meetings)
    result = []

    start = 0

    for s, e in meetings:
        if s == start:
            continue # case if start == 0
        else:
            result.append((start, s))
            start = e

    if meetings[-1][1] != 2359:
        result.append((meetings[-1][1], 2359))
    return result
#print(free_time(meetings))
meetings = [("a", 1, 5, 7), ("b", 5, 7, 6), ("c", 1, 6, 5)]
rooms = [("A", 5), ("B", 6), ("C", 7)] 
def meeting_arrangement(meetings, rooms):
    # sort the meetings by start time ascending
    # sort rooms by limitation ascending
    m = []
    mp = {}
    for name, start, end, people in meetings:
        m.append((start, 1, name, people))
        m.append((end, 0, name, people))
        mp[name] = (start, end)
    m.sort()
    busy = {}
    used = set()
    ans = []
    for time, op, name, people in m:
        if op == 1:
            idx = -1
            for i in range(0, len(rooms)):
                if i in used:
                    continue
                if rooms[i][1] >= people:
                    idx = i
                    break
            if idx == -1:
                print("impossible")
                return []
            else:
                used.add(idx)
                ans.append((name, rooms[idx]))
                busy[mp[name][1]] = idx
        else:
            # release room
            s, e = mp[name]
            idx = busy[e]
            used.remove(idx)
    print(ans)
meeting_arrangement(meetings, rooms)



