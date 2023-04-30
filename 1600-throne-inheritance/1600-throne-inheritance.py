class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.GRAPH = defaultdict(list)    
        self.dead = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.GRAPH[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        order, seen = [], set()
        
        def dfs(parent):
            if parent in seen:
                return
            
            seen.add(parent)
            if parent not in self.dead:
                order.append(parent)
            
            for child in self.GRAPH[parent]:
                dfs(child)
                
            return
        
        dfs(self.king)
        
        return order
                
            
        
        
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()