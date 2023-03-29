class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        
        for i in range(n+1):
            org = i
            while i:
                if i % 2:
                    ans[org] += 1
                i //= 2
                
        return ans