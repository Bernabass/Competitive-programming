class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        arr = [[] for _ in range(numRows)]
        sign, idx = 1, 0
        
        for i in range(n):
            arr[idx].append(s[i])
            if idx == 0:
                sign = 1
                
            if idx == numRows - 1:
                sign = -1
                
            if idx == numRows - 1 == 0:
                sign = 0
                
            idx += sign
                
        ans = []
        for row in arr:
            ans += row
            
        return "".join(ans)