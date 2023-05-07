class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = list(Counter(deck).values())
        x = 0
        
        for val in freq:
            x = gcd(x, val)
            
        return x > 1