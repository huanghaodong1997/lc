# Dumbass question
class Solution:
    def fullJustify(self, words, maxWidth: int):
        
        def getKWords(idx):
            k = 0
            cur_len = 0
            while idx < len(words) and cur_len <= maxWidth:
                cur_len += len(words[idx]) + 1
                idx += 1
                k += 1
            if cur_len <= maxWidth and idx == len(words):
                return k
            if cur_len == maxWidth + 1:
                return k
            return k - 1 if k - 1 > 0 else 1
        
        def insertSpace(lo, hi):
            hi = min(hi, len(words) - 1)
            numWords = hi - lo + 1
            if numWords == 1:
                return words[lo] + " " * (maxWidth-len(words[lo]))
            wordLen = sum(len(word) for word in words[lo:hi+1])
            interval = (maxWidth - wordLen) // (numWords - 1)
            remain = (maxWidth - wordLen) % (numWords - 1)
            total_space = interval * (numWords - 1) + remain
            res = ""
            for i in range(lo, hi+1):
                
                res += words[i]
                if i < hi:
                    space = " " * (interval + 1) if remain > 0 else " " * interval

                    res += space
                    remain -= 1
            return res
        def getLastLine(lo, hi):
            res = ""
            for i in range(lo, hi + 1):
                res += words[i]
                if i < hi:
                    res += " "
            res = res + ' ' * (maxWidth - len(res))
            return res
        i = 0
        ans = []
        while i < len(words):
            k = getKWords(i)
            if i + k < len(words):
                ans.append(insertSpace(i, i+k-1))
            else:
                ans.append(getLastLine(i, i+k-1))
            i += k
        return ans