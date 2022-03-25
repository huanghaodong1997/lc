class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        # After sorting in this way
        # The question boiled down to finding Longest increasing sequence of height
        # Consider [1,4][1,3][1,2] envelopes of same weight could never be LIS
        # [1,3], [2, 4], [3, 2] -> LIS is 3, 4
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)

        def lis(arr):
            dp = []
            
            def binary_search(num):
                lo, hi = 0, len(dp)
                while lo < hi:
                    mi = (lo + hi) // 2
                    if dp[mi] < num:
                        lo = mi + 1
                    else:
                        hi = mi
                        
                return lo
                
            for i in range(0, n):
                idx = binary_search(arr[i])
                if idx == len(dp):
                    dp.append(arr[i])
                else:
                    dp[idx] = arr[i]
            return len(dp)
                    


        return lis([e[1] for e in envelopes])
