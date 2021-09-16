class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        maxArea = 0
        height = [0] * n
        left = [0] * n
        right = [n] * n
        
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                maxArea = max(maxArea, height[j] * (right[j] - left[j]))
        return maxArea