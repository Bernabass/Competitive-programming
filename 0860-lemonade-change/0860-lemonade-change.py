class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        
        for amount in bills:
            if amount == 5:
                fives += 1
                
            elif amount == 10:
                if not fives:
                    return False
                
                fives -= 1
                tens += 1
                
            else:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                    
                elif fives > 2:
                    fives -= 3
                    
                else:
                    return False
                
        return True