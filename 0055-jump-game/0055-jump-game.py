class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @cache
        def dp(idx):
            if idx == n - 1:
                return True
                        
            for jump in range(1, nums[idx] + 1):
                if dp(idx + jump):
                    return True
                
        return dp(0)