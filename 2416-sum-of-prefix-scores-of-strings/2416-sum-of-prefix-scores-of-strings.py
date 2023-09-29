class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            node.count += 1
            
        node.is_end = True
            
    def search(self, word: str) -> bool:
        node = self.root
        count = 0
        
        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]
            count += node.count
            
        return count
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
            
        return True

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        N = len(words)
        trie = Trie()
        ans = [0] * N
        
        for word in words:
            trie.insert(word)
            
        for idx, word in enumerate(words):
            ans[idx] += trie.search(word)
                
        return ans