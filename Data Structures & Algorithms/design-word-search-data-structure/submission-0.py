class TrieNode:
    def __init__(self):
        self.ds = [0] * 26
        self.end = False

class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie 
        for c in word:
            currIdx = ord(c) - ord('a')
            if node.ds[currIdx] == 0:
                node.ds[currIdx] = TrieNode()
            node = node.ds[currIdx]
        node.end = True

    def search(self, word: str) -> bool:
        length = len(word)
        def dfs(node, i):
            if i >= len(word):
                return node.end
            if word[i] == '.':
                #do dfs on every node 
                for n in node.ds:
                    if n != 0:
                        if dfs(n, i + 1):
                            return True
                return False
            else:
                if node.ds[ord(word[i]) - ord('a')] == 0:
                    return False 
                return dfs(node.ds[ord(word[i]) - ord('a')], i + 1)
        return dfs(self.trie, 0)

                

    # at and an add bat
    # a -> false
    # .at -> false 
    # .at -> true 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)