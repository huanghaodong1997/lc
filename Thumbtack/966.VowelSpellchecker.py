from collections import defaultdict
class Solution:
    def spellchecker(self, wordlist, queries):
        
        standard = defaultdict(list)
        vowel = defaultdict(list)
        wordSet = set(wordlist)
        def transform(s):
            tmp = []
            for ch in s:
                if ch in "aeiou":
                    tmp.append('a')
                else:
                    tmp.append(ch)
            return "".join(tmp)
        def duplicateVowels(s):
            # transform to lower
            # transform all vowels
            # remove duplicate vowels
            s = s.lower()
            s = transform(s)
            tmp = []
            i = 0
            while i < len(s):
                if s[i] in "aeiou":
                    curr = s[i]
                    tmp.append(curr)
                    while i < len(s) and s[i] == curr:
                        i += 1
                    
                else:
                    tmp.append(s[i])
                    i += 1
            return "".join(tmp)
        for word in wordlist:
            key = word.lower()
            standard[key].append(word)
            vowel[transform(key)].append(word)
        
        res = []
        
        for q in queries:
            key = q.lower()
            
            if q in wordSet:
                res.append(q)
            # Check capitalization
            elif key in standard:
                res.append(standard[key][0])
            # check vowel
            elif transform(key) in vowel:
                res.append(vowel[transform(key)][0])
            # check repeated vowel
            elif duplicateVowels(key) in vowel:
                res.append(vowel[duplicateVowels(key)][0])
            else:
                res.append("")
        return res

sol = Solution()

wordList = ["KiTe","kite","hare","Hare", "Yellow"]
query = ["kite", "yaaaiilloeew"]

print(sol.spellchecker(wordList, query))
            