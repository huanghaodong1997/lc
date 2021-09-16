def helper(n, res, target, out, idx):
    if idx > n or target < 0:
        return
    if idx == n:
        if target == 0:
            res.append(int(out))
        return
    for i in range(0, 10):
        diff = abs(int(out[-1]) - i)
        helper(n, res, target - diff, out + str(i), idx + 1)
    

        

        
def findNdigitsNums(n, target):
    res = []
    for i in range(1, 10):
        out = str(i)
        helper(n, res, target, out, 1)
    print(res)
findNdigitsNums(3, 10)

