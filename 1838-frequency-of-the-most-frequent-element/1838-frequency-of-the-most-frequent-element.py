class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        total = left = right = size = 0
        curr_val = nums[left]
        while right < n and left < n:
            total += nums[right]
            pos = (right - left + 1)*curr_val - total
            if pos <= k:
                right += 1
            else:
                size = max(size,right - left)   
                total -= nums[left] +nums[right]
                left += 1
                curr_val = nums[left]
        return max(size,right - left)