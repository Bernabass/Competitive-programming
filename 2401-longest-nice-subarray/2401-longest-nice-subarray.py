class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = right = nicest = size = res = 0
        while right < len(nums):
            if not (nums[right] & nicest):
                nicest += nums[right]
                size += 1
            else:
                while (nums[right] & nicest):
                    nicest -= nums[left]
                    size -= 1
                    left += 1
                size += 1
                nicest += nums[right]
                    
            right += 1
            res = max(res,right - left)
        return res