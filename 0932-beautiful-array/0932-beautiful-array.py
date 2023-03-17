class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        def prev_power(n):
            power = 0
            while 2 ** power < n:
                power += 1
                
            return 2 ** (power - 1)

        ans = [1]
        for element in range(2, n+1):
            x = prev_power(element)
            curr = element - x
            idx = ans.index(curr) + 1
            ans.insert(idx, element)
            
        return ans
        
        