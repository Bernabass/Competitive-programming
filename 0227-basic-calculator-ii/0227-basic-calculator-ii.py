class Solution:
    def calculate(self, s: str) -> int:
        num, arr = [], []
        N = len(s)
        operators = {"+", "-", "/", "*"}
        
        for idx, char in enumerate(s):
            if char not in operators:
                if char != " ":
                    num.append(char)
                
            else:
                arr.extend(["".join(num), char])
                num = []
                
            if idx == N - 1:
                arr.append("".join(num))
                
        idx, N = 0, len(arr)
        stack = []
        
        while idx < N:
            char = arr[idx]
            if char in {"*", "/"}:
                a = int(stack.pop())
                idx += 1
                b = int(arr[idx])
                if char == "*":
                    stack.append(str(a*b))
                    
                else:
                    stack.append(str(a//b))
                
            else:
                stack.append(char)
                
            idx += 1
                
        res = idx = 0
        while idx < len(stack):
            char = stack[idx]
            if char not in operators:
                res += int(char)
                
            else:
                idx += 1
                if char == "-":
                    res -= int(stack[idx])
                    
                else:
                    res += int(stack[idx])
                    
            idx += 1
                    
        return res