class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = count = window_sum = 0
        N = len(nums)
        
        for right in range(N):
            while (nums[right] + window_sum) * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1
                
            count += right - left + 1                
            window_sum += nums[right]

        return count            