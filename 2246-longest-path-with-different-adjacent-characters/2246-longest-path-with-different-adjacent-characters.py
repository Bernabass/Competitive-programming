class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        GRAPH = defaultdict(list)
        self.longest_path = 0
        
        for child, parent in enumerate(parent):
            GRAPH[parent].append(child)
        
        def dfs(node):
            info = [0, 0]
            
            for child in GRAPH[node]:
                child_label, child_length = dfs(child)
                
                if child_label != s[node]:
                    if child_length > min(info):
                        idx = info.index(min(info))
                        info[idx] = child_length
                        
            self.longest_path = max(self.longest_path, sum(info)+1)
            
            return s[node], max(info)+1
        
        dfs(0)
        
        return self.longest_path            