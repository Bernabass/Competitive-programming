class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if not n:
            return 0
        
        nums = [0] * (n + 1)
        nums[1] = 1
        max_int = 1
        
        for i in range(2, n + 1):
            quo, rem = divmod(i, 2)
            
            if rem:
                nums[i] = nums[quo] + nums[quo + 1]
                
            else:
                nums[i] = nums[quo]
                
            max_int = max(max_int, nums[i])
            
        return max_int        