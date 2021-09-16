#Working backwards
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y < X: return X - Y

#         If with subtraction and multiplication, the effect of earlier subtraction will be amplified by later multiplications, hence, greedily doing multiplication might not reach optimal solution as an additional early subtraction can have a huge effect.
# Whereas with addition and division, earlier addition will be diminished by later divisions. It is thus always better to do division wherever possible.
        step = 0
        while Y > X:
            step += 1
            if Y % 2 == 1:
                Y += 1
            else:
                Y = Y // 2
        return step + X - Y
        
        