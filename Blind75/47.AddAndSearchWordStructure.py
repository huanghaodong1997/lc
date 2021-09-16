class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.trie
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        # denote that this is a word
        cur.is_word = True
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node.children:
                    if ch == '.':
                        for x in node.children:
                            if search_in_node(word[i + 1:], node.children[x]):
                                return True
                    return False
                else:
                    node = node.children[ch]
            return node.is_word
        return search_in_node(word, self.trie)