class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, len(nums) - 1 
        ptr = 0
        
        while ptr <= right:
            if nums[ptr] == 0:
                nums[ptr], nums[left] = nums[left], nums[ptr]
                left += 1
                ptr += 1
                
            elif nums[ptr] == 2:
                nums[ptr], nums[right] = nums[right], nums[ptr]
                right -= 1
                
            else: 
                ptr += 1