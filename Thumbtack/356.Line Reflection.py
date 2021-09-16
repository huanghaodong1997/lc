def isReflected(points) -> bool:
    if not points:
        return True
    points_x = [x for x,y in points]
    points = set([tuple(p) for p in points])
    # greedy approach, the mid x must satisfied the min_x and max_x
    mid = (min(points_x) + max(points_x)) / 2
    
    for x, y in points:
        mirror_x = mid + (mid - x)
        if (mirror_x, y) not in points:
            return False
    return True

# follow up 1 重复点怎么办, 已经解决

# follow up 2 输入是double 并且有误差范围 怎么办
# 上述方法会产生一条线， 根据误差我们可以尝试多条线，
# 即 会有多条线能满足 min_x, max_x reflection
# loop through 这些线来找答案 [lower bound, upper_bound]
# 比如 mid = 0.0 误差是0.03
# 那么 mid就在 0.0 +- 0.03之间
# 就用 O(n ^ 2)的方法找是否满足在这个误差区间之间

# follow up 3: 不一定是y 轴
# 随便选一个点，然后通过剩下n-1个点找到n-1个可能的线，然后再用之前的算法。