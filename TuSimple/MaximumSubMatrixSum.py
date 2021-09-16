#把二维转换为1维来计算
class Solution:
    def getMaxMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        max_sum = float('-inf')
        bestr1, bestc1 = 0, 0
        ans = [0, 0, 0, 0]
        
        for i in range(0, m):
            b = [0] * n
            for j in range(i, m):
                cur_sum = 0
                for k in range(0, n):
                    
                    b[k] += matrix[j][k]
                    if cur_sum > 0:
                        cur_sum += b[k]
                    else:
                        cur_sum = b[k]
                        bestr1 = i
                        bestc1 = k
                                  
                    if cur_sum > max_sum:
                        max_sum = cur_sum
                        ans[0], ans[1], ans[2], ans[3] = bestr1, bestc1, j, k
        
                
        return ans