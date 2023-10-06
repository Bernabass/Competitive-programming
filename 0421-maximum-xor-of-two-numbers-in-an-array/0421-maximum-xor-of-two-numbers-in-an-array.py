class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_XOR = 0
        
        for idx in range(32, -1, -1):
            max_XOR <<= 1
            prev = set()
            
            for num in nums:
                prev.add(num >> idx)
                
            temp = max_XOR ^ 1
            for curr in prev:
                if temp ^ curr in prev:
                    max_XOR += 1
                    break
                    
        return max_XOR