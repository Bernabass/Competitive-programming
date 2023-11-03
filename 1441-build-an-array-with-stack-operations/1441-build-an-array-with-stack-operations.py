class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        idx = 0
        operations = []
        
        for num in range(1, target[-1] + 1):
            operations.append("Push")
            
            if num != target[idx]:
                operations.append("Pop")
                
            else:
                idx += 1
                
        return operations
        
        """
        
        
        target = [1, 3]
        stack = [1,3]
        
        """