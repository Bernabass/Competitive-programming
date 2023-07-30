class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def back_track(idx):
            if idx == n - 1:
                return 0
            
            ans = float("inf")
            curr = nums[idx]
            if not curr:
                return ans
            
            i = 1
            while i + idx < n and i <= curr:
                ans = min(ans, back_track(idx + i))
                i += 1
                
            return ans + 1
        
        return back_track(0)