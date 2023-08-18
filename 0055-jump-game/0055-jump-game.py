class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @cache
        def dp(idx):
            if idx == n - 1:
                return True
            
            if idx >= n:
                return "heheh"
                        
            for jump in range(1, nums[idx] + 1):
                curr = dp(idx + jump)
                if curr == "heheh":
                    return False
                
                elif curr:
                    return True
                
        return dp(0)