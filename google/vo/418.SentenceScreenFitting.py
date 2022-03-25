class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        next_idx = [0] * n
        freq = [0] * n
        
    #sub-problem: if there's a new line which is starting with certain index in sentence, what is the starting index of next line (nextIndex[]). BTW, we compute how many times the pointer in current line passes over the last index (times[]).
        for i in range(n):
            cur_len = 0
            cur = i
            count = 0
            while cur_len + len(sentence[cur]) <= cols:
                cur_len += len(sentence[cur]) + 1
                cur += 1

                if cur == n:
                    cur = 0
                    count += 1
            # When you come out the while loop
            # You know that after puting all sentences starting from
            # sentence[i], You should put sentence[cur] first at the next line
            next_idx[i] = cur
            freq[i] = count
        
        ans = cur = 0
        for i in range(rows):
            ans += freq[cur]
            cur = next_idx[cur]
        return ans