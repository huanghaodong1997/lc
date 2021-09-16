badge_records = [
["Martha","exit"],
["Paul","enter"],
["Martha","enter"],
["Martha","exit"],
["Jennifer","enter"],
["Paul","enter"],
["Curtis","enter"],
["Paul","exit"],
["Martha","enter"],
["Martha","exit"],
["Jennifer","exit"],
]
from collections import defaultdict
def find(badge_records):
    violate_exit = set()
    violate_enter = set()
    employee = set()
    # 1 -> in the building, 0 outside of the building
    status = defaultdict(int)

    for name, op in badge_records:
        if op == "exit":
            if status[name] == 0:
                violate_enter.add(name)
            status[name] = 0
        if op == "enter":
            if status[name] == 1:
                violate_exit.add(name)
            status[name] = 1
        employee.add(name)
    for e in employee:
        if status[e] == 1:
            violate_exit.add(e)
    return [list(violate_exit), list(violate_enter)]
#print(find(badge_records))
badge_records = [
 ["Paul", 1355],
 ["Jennifer", 1910],
 ["John", 830],
 ["Paul", 1315],
 ["John", 835],
 ["Paul", 1405],
 ["Paul", 1630],
 ["John", 855],
 ["John", 915],
 ["John", 930],
 ["Jennifer", 1335],
 ["Jennifer", 730],
 ["John", 1630],
]
badge_records = [['James', 1300], ['Martha', 1600], ['Martha', 1620], ['Martha', 1530]] 
def timeDifference(a, b):
    aHour = a // 100
    bHour = b // 100
    aMin = a % 100
    bMin = b % 100
    return aHour * 60 + aMin - (bHour * 60 + bMin)

def freq_access(badge_records):
    access_records = defaultdict(list)
    res = {}
    badge_records.sort(key=lambda x:x[1])
    for name, time in badge_records:
        while access_records[name] and timeDifference(time, access_records[name][0]) > 60:
            access_records[name].pop(0)
        access_records[name].append(time)

        if len(access_records[name]) >= 3:
            if name not in res:
                res[name] = access_records[name][:]
            else:
                if len(res[name]) < len(access_records[name]):
                    res[name] = access_records[name][:]
    return res
print(freq_access(badge_records))

