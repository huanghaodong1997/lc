def canConvert(str1: str, str2: str):
    if str1 == str2: return True
    mp = {}
    
    for ch1, ch2 in zip(str1, str2):
        if ch1 in mp and mp[ch1] != ch2:
            return False
        mp[ch1] = ch2
    return True if len(set(mp.values())) < 26 else False
def get_s(str1, str2):
    if str1 == str2: return True
    mp = {}
    
    for ch1, ch2 in zip(str1, str2):
        if ch1 in mp and mp[ch1] != ch2:
            return set()
        mp[ch1] = ch2
    return set(mp.values()) if len(set(mp.values())) < 26 else set()
def get_candidates(str1, str2):
    res = []
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            for ch in "abcdefghijklm":
                tmp = ""
                for i in range(len(str1)):
                
                    if str1[i] == ch1:
                        tmp += ch
                    else:
                        tmp += str1[i]
                    res.append(tmp)
    return res

def min_step(str1, str2):
    if not canConvert(str1, str2): return -1
    q = [(str1, 0)]
    visited = set(str1)

    while q:
        cur_state, step = q.pop(0)
        if cur_state == str2: return step
        candidates = get_candidates(cur_state, str2)
        for candidate in candidates:
            flag = canConvert(candidate, str2)
            if candidate in visited or not flag: continue
            q.append((candidate, step + 1))
            visited.add(candidate)
    return -1
# print(min_step("ab", "ba"))
# print(min_step("ababccc", "ccccccc"))
# print(min_step("aaa", "zzz"))

t_4 = ["abcd", "badc"]
t_7 = ["abcd", "ccdb"]
#t_8 = ["abcdefghijkmabcxyz", "bcdefghijkmabcdbcd"]
t_9 = ["abcdefgi", "bcdefgha"]

#print(min_step(t_4[0], t_4[1]))
print(min_step(t_7[0], t_7[1]))
#print(min_step(t_8[0], t_8[1]))
# print(min_step(t_9[0], t_9[1]))