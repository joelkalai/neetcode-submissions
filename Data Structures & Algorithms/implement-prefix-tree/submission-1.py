class PrefixTree:

    def __init__(self):
        self.start = [0] * 27 

    def insert(self, word: str) -> None:
        node = self.start
        for c in word:
            if node[ord(c) - ord('a')] == 0:
                node[ord(c) - ord('a')] = [0] * 27
            node = node[ord(c) - ord('a')]
        node[26] = 1
            

    def search(self, word: str) -> bool:
        node = self.start
        for c in word:
            if node[ord(c) - ord('a')] == 0:
                return False
            node = node[ord(c) - ord('a')]
        return node[26] == 1
        

    def startsWith(self, prefix: str) -> bool:
        node = self.start
        for c in prefix:
            if node[ord(c) - ord('a')] == 0:
                return False
            node = node[ord(c) - ord('a')]
        return True
        
        