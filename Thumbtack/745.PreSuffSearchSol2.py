class TrieNode():
    def __init__(self):
        self.children = {}
        self.weights = None

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
        node = self.root
        node.weights = i
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.weights = i
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.weights
        
class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        for idx, word in enumerate(words):
            for i in range(len(word), -1, -1):
                tmp = word[i:] + '#' + word
                self.trie.insert(tmp, idx)

    def f(self, prefix: str, suffix: str) -> int:
        w = self.trie.search(suffix + '#' + prefix)
        return w