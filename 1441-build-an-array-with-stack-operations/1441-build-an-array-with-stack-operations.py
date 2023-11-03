class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        hash_target = set(target)
        stack = []
        operations = []
        
        for num in range(1, n + 2):
            if stack and stack[-1] not in hash_target:
                stack.pop()
                operations.append("Pop")
                
            if stack == target:
                return operations
            if num <= n:
                stack.append(num)
                operations.append("Push")
            
        return operations
        
        """
        
        
        target = [1, 3]
        stack = [1,3]
        
        """