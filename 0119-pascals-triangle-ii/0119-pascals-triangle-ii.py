class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        level = [1]
        
        while rowIndex:
            next_level = [1]
            
            for i in range(1, len(level)):
                next_level.append(level[i]+level[i-1])
                
                
            next_level.append(1)
            level = next_level
            rowIndex -= 1
            
        return level