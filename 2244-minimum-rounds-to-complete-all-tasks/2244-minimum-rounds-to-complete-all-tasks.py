class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        min_rounds = 0
        
        for val in freq.values():
            if val == 1:
                return -1
            
            if val % 3 == 0:
                min_rounds += val // 3
            else:
                min_rounds += (val // 3) + 1
        
        return min_rounds