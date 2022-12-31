class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left ,right = 0, 0
        nicest = 0
        size = 0
        res = 0
        while right < len(nums):
            if not (nums[right] & nicest):
                nicest += nums[right]
                size += 1
            else:
                while left <= right:
                    nicest -= nums[left]
                    size -= 1
                    left += 1
                    if not (nums[right] & nicest):
                        size += 1
                        nicest += nums[right]
                        break
                    
            right += 1
            res = max(res,right - left)
        return res