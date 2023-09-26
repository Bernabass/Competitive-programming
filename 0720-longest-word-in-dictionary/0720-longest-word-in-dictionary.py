class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            
        node.is_end = True
            
    def search(self, word: str) -> bool:
        node = self.root
        
        for idx, char in enumerate(word):
            if idx and not node.is_end or char not in node.children:
                return False
            
            node = node.children[char]
            
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
            
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        longest_word = ""
        
        for word in words:
            trie.insert(word)
            
        for word in words:
            if trie.search(word):
                if len(word) > len(longest_word):
                    longest_word = word
                    
                elif len(word) == len(longest_word):
                    longest_word = min(longest_word, word)
                    
        return longest_word       