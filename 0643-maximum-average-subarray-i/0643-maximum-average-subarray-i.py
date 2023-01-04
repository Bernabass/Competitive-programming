class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = window_sum = 0
        n = len(nums)
    
        # Prepraring the fixed sliding window.
        for idx in range(k):
            window_sum += nums[idx]
            right += 1
        max_sum = window_sum
    
        # Maximizing the total sum in the window by sliding it.
        while right < n:
            window_sum += nums[right] - nums[left]
            max_sum = max(max_sum,window_sum)
            right += 1
            left += 1
        
        max_average = max_sum / k
        return max_average   