class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = 1
        values = set(nums)
        
        while count in values:
            count += 1
            
        return count