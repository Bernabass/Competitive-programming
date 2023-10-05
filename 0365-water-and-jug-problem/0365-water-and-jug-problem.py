class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        operations = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]
        target1 = max(targetCapacity, jug1Capacity) - min(targetCapacity, jug1Capacity)
        target2 = max(targetCapacity, jug2Capacity) - min(targetCapacity, jug2Capacity)
        seen = set()

        def dp(curr):
            if curr in seen or curr < 0 or curr >  jug1Capacity + jug2Capacity:
                return False
            
            if curr in {targetCapacity, target1, target2}:
                return True
            
            seen.add(curr)
            ans = False
            
            for oper in operations:
                ans = ans or dp(curr + oper)
                
            return ans
        
        
        return dp(0)
            
            
        