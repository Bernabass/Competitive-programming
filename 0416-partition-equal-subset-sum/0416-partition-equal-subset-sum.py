class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        nums.sort()
        
        if total % 2:
            return False
        
        target, n = total // 2, len(nums)
        ans = [False]
        
        @cache
        def back_track(idx, curr_sum):
            if curr_sum == target:
                ans[0] = True
                
            if idx == n or curr_sum > target:
                return
            
            back_track(idx+1, curr_sum)
            back_track(idx+1, curr_sum + nums[idx])
            
            return
        
        back_track(0, 0)
        
        return ans[0]