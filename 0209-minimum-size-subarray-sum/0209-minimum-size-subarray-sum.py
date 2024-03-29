class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = right = window_sum = 0
        min_len = n + 1
        
        while right < n:
            if window_sum + nums[right] < target:
                window_sum += nums[right]
                right += 1
            else:
                min_len = min(min_len,right-left+1)
                window_sum -= nums[left]
                left += 1
        
        return min_len % (n+1)