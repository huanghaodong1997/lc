from collections import defaultdict
# follow up 多个 users
records = [
    ["browsers", "FireFox", "Chrome"],
    ["systems", "OSX", "Windows"],
    ["types", "Mobile", "Laptop"]
]
def get_subsets(records):
    mp = defaultdict(list)
    for r in records:
        deviceType = r[0]
        for i in range(1, len(r)):
            mp[deviceType].append(r[i])
    keyList = list(mp.keys())
    valueList = []
    for key in keyList:
        valueList.append(mp[key])
    result = []

    def dfs(key_idx, curr_list):
        if key_idx == len(keyList):
            result.append(curr_list[:])
            return 
        key = keyList[key_idx] 
        dfs(key_idx  + 1, curr_list)
        for val in valueList[key_idx]:
            curr_list.append("{}--{}".format(key, val))
            dfs(key_idx + 1, curr_list)
            curr_list.pop()
        return 
    dfs(0, [])
    return result
print(get_subsets(records))
