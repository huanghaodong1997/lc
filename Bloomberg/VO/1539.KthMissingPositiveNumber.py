class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        i, j = 0, len(arr) - 1
        while i <= j:
            pivot = (i + j) // 2
            if arr[pivot] - pivot - 1 < k:
                i = pivot + 1
            else:
                j = pivot - 1
        # At the end of the loop, left = right + 1, and the kth missing number is in-between arr[right] and arr[left].
        # i + k
        # j = i - 1
        # arr[j] + k 减去 arr[j]左边已经缺失的number的数量
        return arr[j] + k - (arr[j] - j - 1) # j + 1 + k = i + k

                