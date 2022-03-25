# dp[i]the number of all possible attendance (without 'A') records with length i :

# end with "P": dp[i-1]
# end with "PL": dp[i-2]
# end with "PLL": dp[i-3]
# end with "LLL": is not allowed
# so dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# the number of all possible attendance (with 'A') records with length n:
# ∑dp[i] *dp[n-1-i] i = 0,1,...,n-1

# Time Complexity O(n)
# Space Complexity O(n)

# (In code nums[i+1] means dp[i])

    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:return 3
        if n==0: return 0
        mod=1000000007
        dp=[0 for i in range(n+1)]
        dp[0],dp[1],dp[2]=1,2,4
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3] )% mod
        res=dp[n] 
        print dp
        for i in range(1,n+1):
            # consider adding one A or not adding, the combination are
            res+=dp[i-1]*dp[n -i]%mod
        res=res%mod
        return res