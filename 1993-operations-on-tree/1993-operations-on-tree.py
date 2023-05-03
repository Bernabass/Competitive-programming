class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.GRAPH, self.locked  = defaultdict(list), defaultdict(int)
        
        for child in range(1, len(parent)):
            self.GRAPH[parent[child]].append(child)
                        
            
    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num]:        
            self.locked[num] = user
            return True
        
        return False
        
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = 0
            return True
        
        return False
        
    def dfs(self, num):
        
        flag = False
        if self.locked[num]:
            flag = True
            self.locked[num] = 0
                
        for adj in self.GRAPH[num]:
            flag = flag | self.dfs(adj)
            
        return flag
            
        
    def unlocked_ancestors(self, num):
        while num != -1:
            if self.locked[num]:
                return False
            
            num = self.parent[num]
            
        return True
            
    def upgrade(self, num: int, user: int) -> bool:
        
        if not self.unlocked_ancestors(num):
            return False
        
        if self.dfs(num):
            self.locked[num] = user
            
            return True
        
        return False