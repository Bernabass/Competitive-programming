class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = -1
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, index) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            
        node.is_end = index
            
    def search(self, word):
        node = self.root
        
        for char in word:
            if node.is_end != -1:
                return node.is_end
            
            if char not in node.children:
                return -1
            
            node = node.children[char]
            
        return -1
    

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        res = sentence.split()
        
        for idx, word in enumerate(dictionary):
            trie.insert(word, idx)
            
        for idx, word in enumerate(res):
            val = trie.search(word)
            
            if val != -1:
                res[idx] = dictionary[val]
                
        return " ".join(res)
                