#math
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
        

# class Solution:
#     def findBestValue(self, arr, target: int) -> int:
#         arr.sort()
#         n = len(arr)
#         cur_sum = 0
#         res = -1
#         min_diff = float('inf')
#         def binary_search(left_bound, right_bound, count, cur_sum):
#             if left_bound + 1 >= right_bound:
#                 return right_bound
#             l, r = left_bound + 1, right_bound
#             while l < r:
#                 mid = (l + r) // 2
#                 mid_diff = abs(cur_sum + mid * count - target)
#                 mid_left = abs(cur_sum + (mid - 1) * count - target) if mid - 1 > left_bound else float('inf')
#                 mid_right = abs(cur_sum + (mid + 1) * count - target) if mid + 1 <= right_bound else float('inf')
#                 if mid_diff < mid_left and mid_diff < mid_right:
#                     return mid
#                 elif mid_diff < mid_left and mid_diff > mid_right:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             return l
#         prev = -1
#         for i, num in enumerate(arr):
#             mutated_num = binary_search(prev, num, n - i, cur_sum)
#             cur_diff = abs(cur_sum + mutated_num * (n - i) - target)
#             if cur_diff < min_diff:
#                 res = mutated_num
#                 min_diff = cur_diff
#             cur_sum += num
#             prev = num
#         return res