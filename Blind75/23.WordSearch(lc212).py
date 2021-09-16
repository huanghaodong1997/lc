class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def insert_trie(self, trie, word):
        curr_node = trie
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode()
            curr_node = curr_node.children[ch]
        #denote end of a word
        curr_node.children['$'] = word
    
    def findWords(self, board, words):
        trie = TrieNode()
        for word in words:
            self.insert_trie(trie, word)
        m = len(board)
        n = len(board[0])
        
        res = []
        def backtrack(x, y, parent):
            letter = board[x][y]
            curr_node = parent.children[letter]
            
            word_match = curr_node.children.pop('$', False)
            
            #if has a match
            if word_match:
                res.append(word_match)
            
            board[x][y] = '#'
            for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                next_x, next_y = x + d[0], y + d[1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or board[next_x][next_y] not in curr_node.children:
                    continue
                backtrack(next_x, next_y, curr_node)
            board[x][y] = letter
            if not curr_node.children:
                parent.children.pop(letter)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    backtrack(i, j, trie)
        return res
            