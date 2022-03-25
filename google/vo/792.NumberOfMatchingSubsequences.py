class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Keep a running dictionary
        # Key is the character that is waiting to be matched
        # Value is a list of substring of word
        # "dog" -> 'd': 'og'
        # suppose s = "daog"
        # iter s, when we met 'd', put 'o' : 'g' , 'a' do nothing, met 'o', put 'g' : '', met 'g', we know we have a match
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append(w[1:])
        res = 0
        for c in s:
            tmp = waiting[c][:]
            waiting[c] = []
            for w in tmp:
                if len(w) == 0:
                    res += 1
                else:
                    waiting[w[0]].append(w[1:])
        return res