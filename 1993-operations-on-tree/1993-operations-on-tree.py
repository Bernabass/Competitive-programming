class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.Tree, self.locked_nodes  = defaultdict(list), defaultdict(int)
        
        for child in range(1, len(parent)):
            self.Tree[parent[child]].append(child)
                        
            
    def lock(self, num: int, user: int) -> bool:
        if not self.locked_nodes[num]:        
            self.locked_nodes[num] = user
            return True
        
        return False
        
    def unlock(self, num: int, user: int) -> bool:
        if self.locked_nodes[num] == user:
            self.locked_nodes[num] = 0
            return True
        
        return False
        
    def unlock_any_descendant(self, num):
        
        flag = False
        if self.locked_nodes[num]:
            flag = True
            self.locked_nodes[num] = 0
                
        for adj in self.Tree[num]:
            flag = self.unlock_any_descendant(adj) or flag
            
        return flag
            
        
    def node_and_ancestors_locked(self, num):
        while num != -1:
            if self.locked_nodes[num]:
                return True
            
            num = self.parent[num]
            
        return False
            
    def upgrade(self, num: int, user: int) -> bool:
        
        if self.node_and_ancestors_locked(num):
            return False
        
        if self.unlock_any_descendant(num):
            
            return self.lock(num, user)
        
        return False