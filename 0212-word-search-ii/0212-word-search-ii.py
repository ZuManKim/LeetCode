class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie(words)
        seen = set()

        def adj(x, y):
            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if 0 <= x + i < m and 0 <= y + j < n:
                    yield (x + i, y + j)
        
        def dfs(prefix, board, x, y):
            char, board[x][y] = board[x][y], '#'

            if trie.search(prefix):
                seen.add(prefix)
                trie.remove(prefix)
            
            for i, j in adj(x, y):
                if board[i][j] != '#':
                    next_prefix = prefix + board[i][j]
                    if trie.starts(next_prefix):
                        dfs(next_prefix, board, i, j)
            
            board[x][y] = char
        
        for i in range(m):
            for j in range(n):
                dfs(board[i][j], board, i, j)

        return seen


class Trie:
    def __init__(self, words=[]):
        self.trie = {}
        for w in words: self.insert(w)
    
    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'
    
    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False
    
    def starts(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True
    
    def remove(self, word):
        t = self.trie
        nodes = []
        for w in word:
            if w not in t: return
            t = t[w]
            nodes.append((t, w))
        
        if '#' in t:
            p = '#'
            for n, w in nodes[::-1]:
                if len(n[p]) == 0 or p == '#': del n[p]
                p = w