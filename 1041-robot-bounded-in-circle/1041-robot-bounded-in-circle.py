class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        def right(x, y):
            return [y, -x]
        
        def left(x, y):
            return [-y, x]
        
        direction = [1, 0]
        coordinate = [0, 0]
        
        for _ in range(100):
        
            for char in instructions:
                if char == "G":
                    coordinate[0] += direction[0]
                    coordinate[1] += direction[1]

                elif char == "R":
                    coordinate = right(coordinate[0], coordinate[1])

                else:
                    coordinate = left(coordinate[0], coordinate[1])
                    
            if coordinate == [0, 0]:
                return True