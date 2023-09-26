class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, val) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            
        node.val = val
            
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return TrieNode()
            
            org = node
            node = node.children[char]
            
        return node

class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        node = self.trie.startsWith(prefix)
            
        return self.dfs(node) + node.val
            
    def dfs(self, node):        
        count = 0
        for adj in node.children.values():
            count += adj.val + self.dfs(adj)
            
        return count
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)