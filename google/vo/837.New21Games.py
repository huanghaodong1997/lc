class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        #For positions x <= K, p[x] = (p[x-1] + p[x-2] + ..... + p[x-W]) * (1/W);
        if N >= K + W - 1:# // all possibilities of positions after alice stops playing are from [K, K+W-1]
            return 1.0
        
        p = [0.0] * (K + W)
        prob = 1 / W
        
        prev = 0
        
        p[0] = 1
        
        for i in range(1, K + 1):
            # minus p[i-W-1] to remove the prob of W step before, because you couldn't go from i - W - 1 to i in one step
            prev = prev - (p[i-W-1] if i-W-1>=0 else 0) + p[i - 1]
            p[i] = prev * prob
            
        req = p[K]
        
        # Key idea, you can never access [K + 1, N] from i >= K + 1
        for i in range(K + 1, N + 1):
            # From K+1, we don't add the p[i-1] term here as it is >= K
            # We decrement the probability because access point > K + 1 will lose the game
            prev = prev - (p[i-W-1] if i-W-1>=0 else 0)
            p[i] = prev * prob
            req += p[i]
        return req