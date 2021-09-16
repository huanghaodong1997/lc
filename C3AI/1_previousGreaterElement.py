temperatures = [10, 15, 15, 25, 30, 35]

def pge(temperatures):
    n = len(temperatures)
    res = [0] * n
    stk = []
    for i, t in enumerate(temperatures):
        while stk and temperatures[stk[-1]] < t:
            stk.pop()

        # Current temperature t is the largest from 0 - i
        if not stk:
            res[i] = i + 1
        else:
            res[i] = i - stk[-1]
        stk.append(i)
    return res

print(pge(temperatures))

# So at each position, we only care about 
# the position of previous larger element then element in current position
# So we can use a monotonic stack with a non-increasing order
# To get how many consecutive smaller or equal elements before
# The current elemnt