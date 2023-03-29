class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        
        for i in range(n+1):
            org = i
            if i % 2:
                ans[org] += 1
            i //= 2
            ans[org] += ans[i]
                
        return ans