# Smallest
class Smallest:
    def smallestPerimeter(self, A):
        A.sort()
        for i in range(0, len(A) - 2):
            j, k = i + 1, i + 2
            while k < len(A) and A[i] + A[j] <= A[k]:
                j += 1
                k += 1
            if k < len(A) and A[i] + A[j] > A[k]:
                return (A[i], A[j], A[k])
        return 0
# Largest
class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0

s = Smallest()
A = [2,3,5,7,9]
print(s.smallestPerimeter(A))