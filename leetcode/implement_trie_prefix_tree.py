# https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.TrieNodes = {}
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for c in word:
            current.TrieNodes[c] = current.TrieNodes.get(c, TrieNode())
            current = current.TrieNodes[c]
        current.isWord = True
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for c in word:
            if not c in current.TrieNodes:
                return False
            current = current.TrieNodes[c]
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for c in prefix:
            if not c in current.TrieNodes:
                return False
            current = current.TrieNodes[c]
        return True
