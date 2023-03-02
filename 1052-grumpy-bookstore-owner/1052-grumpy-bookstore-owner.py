class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        when_grumpy = when_happy = 0
        N = len(customers)
        
        for idx in range(minutes):
            if grumpy[idx]:
                when_grumpy += customers[idx]
                
            else:
                when_happy += customers[idx]
                
        max_change_to_happiness = when_grumpy
                
        for curr in range(minutes, N):
            if not grumpy[curr]:
                when_happy += customers[curr]
                
            else:
                when_grumpy += customers[curr]
                
            if grumpy[curr-minutes]:
                when_grumpy -= customers[curr-minutes]
            
            max_change_to_happiness = max(max_change_to_happiness, when_grumpy)
               
                                    
        return when_happy + max_change_to_happiness
                
            
            
            
            
            
            