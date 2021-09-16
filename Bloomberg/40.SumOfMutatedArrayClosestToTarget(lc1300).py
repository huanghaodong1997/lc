class Solution:
    def findBestValue(self, arr, target: int) -> int:
        arr.sort(reverse=True)
        maxA = arr[0]
        
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        if not arr:
            return maxA
        if target / len(arr) - target // len(arr) <= 0.5:
            return target // len(arr)
        return target // len(arr) + 1
        