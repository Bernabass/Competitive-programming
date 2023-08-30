class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        idx = len(nums) - 2
        prev = nums[-1]
        operations = 0
        
        while idx >= 0:
            n = ceil(nums[idx] / prev)
            operations += n - 1
            prev = nums[idx] // n
                
            idx -= 1
            
        return operations