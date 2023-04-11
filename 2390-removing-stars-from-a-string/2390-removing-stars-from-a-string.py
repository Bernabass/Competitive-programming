class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for val in s:
            if val == "*":
                stack.pop()
                continue
        
            stack.append(val)
            
        return "".join(stack)