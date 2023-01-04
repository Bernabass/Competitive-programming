class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = total = 0
        n = len(nums)
    
        # Prepraring the fixed sliding window
        for idx in range(k):
            total += nums[idx]
            right += 1
        max_sum = total
    
        # Maximizing the total sum in the window by sliding it.
        while right < n:
            total += (-1 * nums[left] ) + nums[right]
            max_sum = max(max_sum,total)
            right += 1
            left += 1
        
        max_average = max_sum / k
        return max_average   