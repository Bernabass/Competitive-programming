class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = [("(", 1, 0)]
        
        while stack:
            curr, left, right = stack.pop()
            if left - right < 0 or left > n or right > n:
                continue
                
            if left == right == n :
                ans.append(curr)
                
            stack.append((curr + "(", left + 1, right))
            stack.append((curr + ")", left, right + 1))
            
        return ans