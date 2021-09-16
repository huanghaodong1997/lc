# Simulation的解法
class Solution:
    def lastRemaining(self, n: int) -> int:
        
        head, step = 1, 1
        
        direction = True
        
        while n > 1:
            if direction or (not direction and n % 2 == 1):
                head += step
            step *= 2
            n = n // 2
            direction = False if direction else True
        return head

# Math的方法， 利用一个有序数组mirro的特性， 从左边eliminate最后得到的值 和 从右边eliminate最后得到的值对称， 
# lastRemaining(n, 左)  + lastRemaining(n, 右) = n + 1
# 因为mirror的特点， lastRemaning(n)的值会是  lastRemaining(n/2)从右边开始数的值，所以答案是
# LastRemaning(n) = 2 * (1 + n / 2 - lastRemaining(n / 2))
# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         return 1 if n == 1 else 2 * (1 + n // 2 - self.lastRemaining(n // 2));