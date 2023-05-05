class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:            
        n = len(nums)
        ans = []
        
        def back_track(start):
            if start == n-1:
                ans.append(nums.copy())
                
                return 
            
            for idx in range(start, n):
                
                nums[start], nums[idx] = nums[idx], nums[start]
                back_track(start+1)
                nums[start], nums[idx] = nums[idx], nums[start]

        back_track(0)
        
        return ans