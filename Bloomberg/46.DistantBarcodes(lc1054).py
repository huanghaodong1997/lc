from collections import Counter
# Greedily arrange the most frequent elements, until reach the end, then start from 1, arrange the remain elements
class Solution:
    def rearrangeBarcodes(self, barcodes):
        c = Counter(barcodes)
        i, n = 0, len(barcodes)
        for num, freq in c.most_common():
            for _ in range(freq):
                barcodes[i] = num
                i += 2
                if i >= n : i = 1
        return barcodes