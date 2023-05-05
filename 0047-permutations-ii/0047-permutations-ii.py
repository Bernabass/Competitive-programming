class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        def back_track(path, num):
            if not num:
                temp = tuple(path)
                if temp not in res:
                    res.add(temp)   
                return
            
            for i in range(len(num)):
                back_track(path+[num[i]], num[:i] + num[i+1:]) 
        
        back_track([], nums)
        
        return res