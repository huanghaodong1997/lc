def can_be_written(n):
    # (3 a + 2b) * 3 + 20 c = n
    # n % 3 == 0
    # n >= 20 and n % 20 == 0
    arr = []
    for i in range(0, 10):
        for j in range(0, 10):
            arr.append(3 * i + 2 * j)
    return list(sorted(arr))
print(can_be_written(10))

# 3a + 20b = n: a >= 2

# 6 以上 能被 3整除的数 -> 可以
# 20 以上 能被 20整除的数 -> 可以
# 写一个for 循环 b 从 1 到 n // 20: 若 n - 20 b 可以被 3整除， 即为所求 naive

#prove: (3a+2b)*3 + 20c = n
# n = 3m + k
#(3a+2b)*3 + 20c = 3 * m + k, k 为 【0，1，2】余数
#(1) if k == 0: 满足
#(2) if k == 1: 即 n 可以被表达成 3m + 1 时
#   let c == 2: (3a + 2b + 13) * 3 + 1 = n  , 3a + 2b > 1
#   所以 n >= 40(a=b=0, c= 2), n % 3 == 1 且 n != 43 时 满足
#(3) if k == 2: n = 3m + 2
#   let c == 1:
#    (3a + 2b + 6) * 3 + 2 = n, 3a + 2b > 1
#   n >= 20, n != 23 时 满足

# 对于任意大于 43 的数， 均满足这个性质

