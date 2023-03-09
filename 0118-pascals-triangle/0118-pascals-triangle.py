class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        level = [1]
        res = [level]
        while numRows -1:
            next_level = [1]
            
            for i in range(1, len(level)):
                next_level.append(level[i]+level[i-1])
                
                
            next_level.append(1)
            level = next_level
            if level:
                res.append(level)
            numRows -= 1
            
        return res