class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:    
        ans = []
        
        def back_track(arr, res):
            if not nums:
                ans.append(res.copy())
            
            for idx, num in enumerate(nums):
                res.append(num)
                nums.remove(num)
                back_track(nums, res)
                nums.insert(idx, num)
                res.pop()
                
            return
        
        back_track(nums, [])
        
        return ans