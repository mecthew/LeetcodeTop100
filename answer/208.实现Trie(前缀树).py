from typing import List
# Medium
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.trie
        for ch in word:
            if ch not in root:
                root[ch] = {}
            root = root[ch]
        root['is_word'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.trie
        for ch in word:
            if ch not in root:
                return False
            root = root[ch]
        return 'word' in root

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.trie
        for ch in prefix:
            if ch not in root:
                return False
            root = root[ch]
        return True
