class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        
        for num in range(n+1):
            org = num
            ans[num] += 1 & num
            num >>= 1
            ans[org] += ans[num]
                
        return ans