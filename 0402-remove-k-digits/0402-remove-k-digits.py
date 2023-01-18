class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans_size = len(num) - k
        order = int(num)
        ans = []
        
        for digit in num:
            while k and ans and digit < ans[-1]:
                ans.pop()
                k -= 1
            
            ans.append(digit)
          
        ans =  "".join(ans[:ans_size])
        ans = ans.lstrip("0")
        if not ans:
            return "0"
        
        return ans