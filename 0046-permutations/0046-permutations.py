class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:            
        res = []
        def back_track(path, num):
            if not num:
                res.append(path)   
                return
            
            for i in range(len(num)):
                back_track(path + [num[i]], num[:i] + num[i+1:]) 
        
        back_track([], nums)
        
        return res