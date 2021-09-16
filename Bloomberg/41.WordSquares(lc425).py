class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.words = []
    
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode()
            curr_node = curr_node.children[ch]
            curr_node.words.append(word)
        curr_node.is_word = True
        
    def getWordsWith(self, prefix):
        curr_node = self.root
        for ch in prefix:
            if ch not in curr_node.children: return []
            curr_node = curr_node.children[ch]
        return curr_node.words

class Solution:
    def wordSquares(self, words):
        if not words: return []
        trie = Trie()
        n = len(words[0])
        for word in words:
            trie.insert(word)
        ans = []
        word_square = []
        
        def backtracking(depth):
            if depth == n:
                ans.append(word_square[:])
                return 
            prefix = "".join(word[depth] for word in word_square)
            candidates = trie.getWordsWith(prefix) if prefix != "" else words
            for c in candidates:
                word_square.append(c)
                backtracking(depth + 1)
                word_square.pop()
        backtracking(0)
        return ans
            
            
            