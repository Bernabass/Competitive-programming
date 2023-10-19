class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def do(arr):
            stack = []
            for char in arr:
                if char == "#":
                    if stack:
                        stack.pop()
                        
                else:
                    stack.append(char)
                    
            return "".join(stack)
        
        return do(s) == do(t)
        
        
        