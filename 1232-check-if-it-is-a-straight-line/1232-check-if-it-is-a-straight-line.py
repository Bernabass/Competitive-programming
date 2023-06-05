class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        vertical = coordinates[0][0] - coordinates[1][0]
        
        if vertical:
            slope = (coordinates[0][1] - coordinates[1][1]) / vertical
        
        for i in range(len(coordinates)):
            change_x = coordinates[i][0] - coordinates[i-1][0]
            if vertical == 0:
                if change_x == 0:
                    continue
                    
                else:
                    return False
                
            change_y = coordinates[i][1] - coordinates[i-1][1]
            
            if not change_x:
                return False
            curr_slope = change_y / change_x
            if curr_slope != slope:
                return False
            
        return True