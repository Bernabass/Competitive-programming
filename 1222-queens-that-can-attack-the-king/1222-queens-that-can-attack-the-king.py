class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set(map(tuple,queens))
        neighbours = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        direct_attackers = []
        next_position = tuple(king)
    
        for row, col in neighbours:
            next_position = tuple(king)
            while 0 <= next_position[0] < 8 and  0 <= next_position[1] < 8:
                if next_position in queens:
                    direct_attackers.append(next_position)
                    break
                next_position = (next_position[0] + row, next_position[1] + col)
        
        return direct_attackers