class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def back_track(path, num):
            if not num:
                res.append(path.copy())
            
            for i in range(len(num)):
                if i and num[i] == num[i-1]:
                    continue
                    
                back_track(path + [num[i]], num[:i] + num[i+1:])
                          
        
        back_track([], nums)
        
        return res