class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def comb(prev, ketay):
            if len(prev) == k:
                ans.append(prev.copy())
                return
            
            if ketay == n:
                return
                
            
            ketay += 1
            prev.append(ketay)
            comb(prev, ketay)
                
            prev.pop()
            comb(prev, ketay)
            
            return
        
        
        comb([], 0)
        
        return ans