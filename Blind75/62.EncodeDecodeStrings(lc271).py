#encode this with  lengthOfword + ','(serve as seperator) + word
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for word in strs:
            res += (str(len(word)) + ',' + word)
        return res

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        
        res = []
        i = 0
        while i < len(s):
            comma = s.index(',', i)
            num_ch = int(s[i:comma])
            res.append(s[comma + 1:comma + 1 + num_ch])
            i = comma + num_ch + 1
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))