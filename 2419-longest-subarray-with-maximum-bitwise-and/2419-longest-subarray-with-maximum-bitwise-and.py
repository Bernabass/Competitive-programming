class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_AND = max(nums)
        count = ans = 0
        
        for num in nums:
            count = (count + (num == max_AND)) * (num == max_AND)
            ans = max(count, ans)
            
        return ans
            
            