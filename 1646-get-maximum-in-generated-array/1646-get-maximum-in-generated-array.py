class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return 0
        
        nums = [0] * (n + 1)
        nums[1] = max_int = 1
        
        for i in range(2, n + 1):
            prev, rem = divmod(i, 2)
            nums[i] = nums[prev] + nums[prev + 1] * rem
                
            max_int = max(max_int, nums[i])
            
        return max_int