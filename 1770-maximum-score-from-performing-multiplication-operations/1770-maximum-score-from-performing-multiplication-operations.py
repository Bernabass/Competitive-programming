class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        
        @cache
        def back_track(left, idx):
            if idx == m:
                return 0
            
            right = n + left - (idx + 1)
            sum1 = multipliers[idx]*nums[left] + back_track(left+1, idx+1)
            sum2 = multipliers[idx]*nums[right] + back_track(left, idx+1)
            
            return max(sum1, sum2)
        
        return back_track(0, 0)