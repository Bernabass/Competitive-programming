class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        pair_skill = total_skill / (len(skill)/2)
        group = Counter(skill)
        chemistry = 0
        
        for player in skill:
            mate = pair_skill - player
            if mate in group and group[mate] > 0:
                chemistry += player * mate
                group[mate] -= 1
            else:
                return -1
            
            
        return int(chemistry/2)   