class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort()
        prev_product, prev_sum =  0, 0
        n , ind= len(s), 1
        
        for i in range(n):
            prev_product += (i + 1) * s[i]
            prev_sum += s[i]
            
        ans = max(0, prev_product)
        while ind < n:
            prev_sum -= s[ind - 1]
            prev_product -= (s[ind - 1] + (prev_sum))
            
            ans = max(ans, prev_product)
            ind += 1
            
        return ans
            
            