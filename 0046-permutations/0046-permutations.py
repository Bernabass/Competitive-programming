class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:    
        ans = []
        
        def back_track(used, res):
            if len(used) == len(nums):
                
                ans.append(res.copy())
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    res.append(num)
                    back_track(used, res)
                    used.remove(num)
                    res.pop()
                    
            return
        
        back_track(set(), [])
        
        return ans