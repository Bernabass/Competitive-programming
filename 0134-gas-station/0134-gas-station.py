class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, current_sum, total_sum = 0, 0, 0
        n = len(gas)
        for i in range(n):
            current_sum += gas[i] - cost[i]
            if current_sum < 0:
                start = i + 1
                current_sum = 0
            total_sum += gas[i] - cost[i]
        return start if total_sum >= 0 else -1
        
        '''0 -  0 + 1 = 1
        1 - 3 + 2 = 0
        0 - 4 + 3 = -1
        -1 - 5 + 4 = -2
        -2 - 1 + 5 = 2
        2 - 2 + 1 = 1
        
        [1,0,-1,-2,2]
        [3,4, 5, 1,2]
        [1,2, 3, 4,5]
        1 -3 + 2 = 0'''