class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0
        N = len(nums)
        
        for val in nums:
            if not val:
                red += 1
            elif val == 1:
                white += 1
            else:
                blue += 1
                
        for idx in range(N):
            if red:
                nums[idx] = 0
                red -= 1
                
            elif white:
                nums[idx] = 1
                white -= 1
            
            else:
                nums[idx] = 2
                blue -= 1          