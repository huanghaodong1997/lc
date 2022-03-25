class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]  # record value and index
        result = [0] * n
        
        def mergesort(arr, left, right):
            if right - left <= 1:
                return
            mid = (left + right) // 2
            mergesort(arr, left, mid)
            mergesort(arr, mid, right)
            merge(arr, left, right, mid)
            
        # merge arr[left:mid] and arr[mid:right]
        def merge(arr, left, right, mid):
            i = left
            j = mid
            
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid represent how many number jump to left side of arr[i]
                    result[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    # smaller element move to left of arr[i], incerment j, now j - mid also increase
                    j += 1
            
            # when one of the subarrays is empty
            
            while i < mid:
                # j - mid numbers jump to the left side of arr[i]
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            
            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]
                
        mergesort(arr, 0, n)
        
        return result     