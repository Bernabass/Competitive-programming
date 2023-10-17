class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def dp(idx, flag):
            if idx == N:
                return 0
            
            pick = no_pick = -inf
            no_pick = dp(idx + 1, flag)

            if flag:
                pick = -nums[idx] + dp(idx + 1, 1 - flag)

            else:
                pick = nums[idx] + dp(idx + 1, 1 - flag)

            return max(pick, no_pick)
        
        return dp(0, 0)