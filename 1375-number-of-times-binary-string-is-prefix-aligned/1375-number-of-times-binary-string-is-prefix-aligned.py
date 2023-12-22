class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        N = len(flips)
        curr_sum = ans = 0
        
        for idx in range(N):
            curr_sum = max(curr_sum, flips[idx])
            if curr_sum == idx + 1:
                ans += 1
            
        return ans