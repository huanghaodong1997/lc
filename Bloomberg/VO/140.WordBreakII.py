#The same word in the dictionary may be reused multiple times in the segmentation.
#You may assume the dictionary does not contain duplicate words.
class DFSMemoSolution:
    def wordBreak(self, s: str, wordDict):
        # intialize the ending case
        # when i = len(s), dp[i] should contain an empty string
        # dp[i]: the word u can form using s[i:]

        memo = {len(s) : ['']}
        word_set = set(wordDict)
        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = []
            for j in range(i + 1, len(s) + 1):
                prefix = s[i:j]
                if prefix in word_set:
                    for word in dp(j):
                        if word != '':
                            memo[i].append(prefix + ' ' + word)
                        # Reach end of s, u can simply append the result
                        else:
                            memo[i].append(prefix)
            return memo[i]
        return dp(0)
#the bottom-up dynamic programming progressively 
# builds up the solutions for the sub-problems upfront, 
# rather than delaying them to the end.
class DPSolution:
    def wordBreak(self, s: str, wordDict):
        n = len(s)
        if set(s) > set(''.join(wordDict)):
            return []
        memo = [[] for _ in range(n + 1)]
        memo[n].append('')
        
        # memo[i]: words that can be formed using s[i: n]
        # the answer we want: memo[0]

        # The fist loop is endIndex
        # We build the result from the end of list
        # imagine that if s[i:n] exist in wordDict
        # then s[i:n] must be in memo[i] because it will be the last word
        
        # for some j, i < j < n
        # s[j:n] in wordDict, s[i:j] in wordDict
        # So s[i:j] s[j:n] in memo[i]
        # s[i:j] (for subsentence in memo[j])
        
        # We continue the process by concatening the words
        for j in range(n, 0, -1):
            # The second loop is startIndex
            for i in range(j - 1, -1, -1):
                prefix = s[i:j]
                
                # concatenting s[i:j] to all words in memo[j]
                if prefix in wordDict:
                    for word in memo[j]:
                        if word != '':
                            memo[i].append(prefix + ' ' + word)
                        else:
                            memo[i].append(prefix)
        return memo[0]