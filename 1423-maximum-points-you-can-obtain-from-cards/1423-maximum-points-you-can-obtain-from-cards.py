class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_size = n - k
        minn = prev = sum(cardPoints[:window_size])
        
        for idx in range(window_size,n):
            curr_sum = prev - cardPoints[idx-window_size] + cardPoints[idx]
            minn = min(minn,curr_sum)
            prev = curr_sum
         
        return total - minn