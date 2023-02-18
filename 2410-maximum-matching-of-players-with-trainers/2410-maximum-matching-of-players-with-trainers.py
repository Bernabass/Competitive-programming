class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse = True)
        trainers.sort(reverse = True)
        max_match = 0
        
        while players and trainers:
            if players[-1] <= trainers[-1]:
                max_match += 1
                players.pop()
                
            trainers.pop()
                 
        return max_match