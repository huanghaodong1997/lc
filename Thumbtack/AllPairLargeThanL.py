A = [8, 5, 12, 3, 4]
L = 2
M = 2
# (8, 3) (8, 4) (5, 4)
import heapq
# O(n * n * (m log m)) heap
# O(n * 2) + O(n^2 logn^2) 
def max_sum(A, L, M):
    h = []
    for i in range(0, len(A) - L - 1):
        for j in range(i + L + 1, len(A)):
            heapq.heappush(h, (A[i] + A[j]))
            if len(h) > M:
                heapq.heappop(h)
    res = []
    while h:
        res.append(heapq.heappop(h))
    return res[::-1]
#print(max_sum(A, L, M))

# // Return the maximum sum of two elements in arr whose 
# // indices differ by at least distance. 
# int max_distant_sum(int[] arr, int distance) { 
#     if (arr.length <= distance) { 
#         // The array is too small. There is no such sum. 
#         return 0; 
#     } 
#     int max_elem = arr[0]; 
#     int max_sum = arr[0] + arr[distance]; 
#     for (int i = distance; i < arr.length; i++) { 
#         // max_elem is the maximum value encountered at least 
#         // distance indices previously. 
#         max_elem = max_elem > arr[i-distance] ? max_elem : arr[i-distance]; 
#         // max_sum is the maximum allowed sum using elements 
#         // up to index i. 
#         max_sum = max_sum > arr[i] + max_elem ? max_sum : arr[i] + max_elem; 
#     } 
#     return max_sum; 
# } 


